import os
import requests
import traceback
from tqdm import tqdm
import json


def request_info(url):
    response   = requests.get(url)
    try:
        resp_str = str(response.content, encoding="utf-8")
        data = json.loads(resp_str)
    except json.decoder.JSONDecodeError as e:
        print(f"Server error: {resp_str}")
        return None

    if response.status_code != 200:
        print(f"Request failed, {data['detail']}")
        return None
    
    return data


def upload_file(url, file, headers, title, chunk_size=4096*100):

    if isinstance(file, str):
        file = open(file, "rb")
        
    file.seek(0, 2)
    file_size = file.tell()
    file.seek(0)

    def gen_stream_file():
        progress = tqdm(total=file_size, unit='B', unit_scale=True, desc=title)
        while True:
            chunk = file.read(chunk_size)
            progress.update(len(chunk))

            if len(chunk) == 0:
                break
            
            yield chunk

        progress.close()

    try:
        response = requests.post(url, data=gen_stream_file(), headers=headers)
    except requests.exceptions.ConnectionError as e:
        print("By default, the max upload file size is: 5 MB")
        return None

    content_string = str(response.content, encoding="utf-8")
    try:
        data = json.loads(content_string)
    except json.decoder.JSONDecodeError as e:
        print(f"Upload failed, {content_string}")
        return None

    if response.status_code != 200:
        msg = data["detail"]
        print(f"Upload failed, {msg}")
        return None
    
    return data


def request_rawdata(url):
    try:
        response   = requests.get(url)
        if response.status_code != 200:
            msg = json.loads(str(response.content, encoding="utf-8"))["detail"]
            print(f"Download failed, {msg}")
            return None
        return response.content
    except Exception as e:
        traceback.print_exc()
    return None


def request_file(url, file, title, chunk_size=4096*100):
    
    try:
        response   = requests.get(url, stream=True)
        if response.status_code != 200:
            msg = str(response.content, encoding="utf-8")
            try:
                msg = json.loads(msg)["detail"]
            except json.decoder.JSONDecodeError as e:
                pass
                
            print(f"Download failed, {msg}")
            return False

        content_iter = response.iter_content(chunk_size=chunk_size)
        content_length = int(response.headers["Content-Length"])
        progress = tqdm(total=content_length, unit='B', unit_scale=True, desc=title)

        if isinstance(file, str):
            file = open(file, "wb")

        for chunk in content_iter:
            file.write(chunk)
            progress.update(len(chunk))

        return True
    except Exception as e:
        traceback.print_exc()
    return False