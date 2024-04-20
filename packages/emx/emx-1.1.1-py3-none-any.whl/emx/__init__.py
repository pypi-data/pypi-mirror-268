'''
    Copy right 2023.
'''

import sys
import argparse
import os
import platform
from urllib.parse import urlencode
from . import http
import zipfile
import tempfile
import shutil
from tqdm import tqdm
import json
import re
import getpass

verbose = False

def encode_password(user_name, pwd):
    import hashlib
    m = hashlib.md5()
    m.update(f"User:{user_name}, PWD:{pwd}".encode("utf-8"))
    return m.hexdigest()

def get_python_link_name(pydll_path, os_name):
    if os_name == "linux":
        for so in os.listdir(pydll_path):
            if so.startswith("libpython") and not so.endswith(".so") and so.find(".so") != -1:
                basename = os.path.basename(so[3:so.find(".so")])
                full_path = os.path.join(pydll_path, so)
                return basename, full_path
    return None, None

def format_size(size):

    units = ["Byte", "KB", "MB", "GB", "PB"]
    for i, unit in enumerate(units):
        ref = 1024 ** (i + 1)
        if size < ref:
            div = 1024 ** i
            if i == 0:
                return f"{size} {unit}"
            else:
                return f"{size / div:.2f} {unit}"
    return f"{size} Bytes"

class ChangeCWD:
    def __init__(self, dir):
        self.dir = os.path.abspath(dir)
        self.old = os.path.abspath(os.getcwd())
    
    def __enter__(self):
        os.chdir(self.dir)
        if verbose:
            print(f"Enter {self.dir}")

    def __exit__(self, *args, **kwargs):
        os.chdir(self.old)
        if verbose:
            print(f"Leave {self.dir}, Enter {self.old}")


class Cmd:
    def __init__(self, actions):
        self.parser    = argparse.ArgumentParser()
        self.subparser = self.parser.add_subparsers(dest="cmd")
        self.actions   = actions

    def add_cmd(self, name : str, help : str = None)->argparse._ActionsContainer:
        return self.subparser.add_parser(name, help=help)

    def help(self):
        self.parser.print_help()

    def hello(self):
        print(
            "You can use 'emx --help' to show the more message."
        )

    def run(self, args, remargs):
        args = self.parser.parse_args(args)
        if args.cmd is None:
            self.hello()
            return False

        return self.actions.private_run_cmd(args, remargs)


class Config:
    def __init__(self):

        self.SERVER_IP   = "www.zifuture.com"
        self.SERVER_PORT = 8000
        self.SERVER      = f"http://{self.SERVER_IP}:{self.SERVER_PORT}"
        self.CACHE_ROOT  = os.path.expanduser('~/.cache/emx')
        self.CACHE_FILE  = os.path.join(self.CACHE_ROOT, "config.json")
        self.OS_NAME     = platform.system().lower()
        self.PY_VERSION  = ".".join(sys.version.split(".")[:2])
        self.EMX_ROOT   = os.path.realpath(os.path.dirname(os.path.abspath(__file__)))
        self.CWD         = os.path.abspath(os.path.curdir)
        self.PYLIB_DIR   = os.path.join(sys.exec_prefix, "lib")
        self.PYLIB_NAME, self.PYLIB_PATH = get_python_link_name(self.PYLIB_DIR, self.OS_NAME)
        self.config       = {}
        if not os.path.exists(self.CACHE_FILE):
            os.makedirs(self.CACHE_ROOT, exist_ok=True)
        else:
            try:
                self.config = json.load(open(self.CACHE_FILE))
                if not isinstance(self.config, dict):
                    self.config = {}
            except Exception as e:
                print(f"Failed to load config file: {self.CACHE_FILE}")

        user_token = self.config.get("UserToken", None)
        user_name  = self.config.get("UserName", None)
        if user_name is None:
            self.login()

        self.SERVER_IP   = self.config.get("SERVER_IP", self.SERVER_IP)
        self.SERVER_PORT = self.config.get("SERVER_PORT", self.SERVER_PORT)
        self.SERVER_IP   = os.environ.get("EMX_SERVER_IP", self.SERVER_IP)
        self.SERVER_PORT = os.environ.get("EMX_SERVER_PORT", self.SERVER_PORT)
        self.SERVER      = f"http://{self.SERVER_IP}:{self.SERVER_PORT}"

        os.environ["EMX_SERVER_IP"] = self.SERVER_IP
        os.environ["EMX_SERVER_PORT"] = str(self.SERVER_PORT)
        os.environ["EMX_SERVER"] = self.SERVER

    def login(self):
        while True:
            user_name = input(f"Please input your UserName: ")
            if len(user_name) < 3 or not user_name.isalnum():
                print(f"Invalid username[{user_name}] was entered. The password length must be greater than or equal to 3 and only [a-zA-Z0-9] can be accepted.")
            else:
                break
        
        user_pwd = None
        while True:
            user_pwd = getpass.getpass(f"Please input your Password: ")
            if len(user_pwd) < 3:
                print(f"Password length must be greater than or equal to 3")
            else:
                break
        
        self.config["UserToken"] = encode_password(user_name, user_pwd)
        self.config["UserName"]  = user_name
        json.dump(self.config, open(self.CACHE_FILE, "w"))
        print(f"Successfully logged with [{user_name}].")

    def get_cfg(self, name):
        return self.config.get(name, None)
    
    def set_cfg(self, name, value):
        self.config[name] = value
        json.dump(self.config, open(self.CACHE_FILE, "w"))

    def __repr__(self):
        sb  = ["Config:"]
        dic = self.get_dict()
        for key in dic:
            val = dic[key]
            sb.append(f"   {key} = {val}")
        return "\n".join(sb)


class Actions:
    def __init__(self, app):
        self.app = app
        self.cfg : Config = app.cfg

    def private_run_cmd(self, args, remargs):
        
        cmd = args.cmd
        if not hasattr(self, cmd):
            return False

        del args.__dict__["cmd"]
        self.remargs = remargs
        return getattr(self, cmd)(args)

    def list(self, args : argparse.Namespace):
        key = args.key
        show_count = args.count
        show_skip  = args.skip

        req_args = urlencode({
            "keyword": key, 
            "type": "path", 
            "show_count": show_count,
            "show_skip": show_skip,
            "ftype": "files",
            "user_name": self.cfg.get_cfg("UserName"),
            "user_token": self.cfg.get_cfg("UserToken")
        })
        
        resp = http.request_info(f"{self.cfg.SERVER}/search?{req_args}")
        if resp is None:
            return False
        
        files = resp["files"]
        print(f"Found {len(files)} files by {key}:")
        for i, file in enumerate(files):
            path = file["path"]
            size = int(file["size"])
            desc = file["descript"]
            short_id = file["id"]
            permission = file["permission"]
            download_counter = file["download_counter"]
            if desc:
                print(f"{short_id}. {path} [{format_size(size)}]: {desc}, download[{download_counter}], {permission}")
            else:
                print(f"{short_id}. {path} [{format_size(size)}], download[{download_counter}], {permission}")

    def cmds(self, args : argparse.Namespace):
        key = args.key
        show_count = args.count
        show_skip  = args.skip

        req_args = urlencode({
            "keyword": key, 
            "type": "name", 
            "show_count": show_count,
            "show_skip": show_skip,
            "ftype": "cmds",
            "user_name": self.cfg.get_cfg("UserName"),
            "user_token": self.cfg.get_cfg("UserToken")
        })
        
        resp = http.request_info(f"{self.cfg.SERVER}/search?{req_args}")
        if resp is None:
            return False
        
        files = resp["files"]
        print(f"Found {len(files)} files by {key}:")
        for i, file in enumerate(files):
            path = file["path"]
            size = int(file["size"])
            desc = file["descript"]
            short_id = file["id"]
            download_counter = file["download_counter"]
            if desc:
                print(f"{short_id}. {path} [{format_size(size)}]: {desc}, download[{download_counter}]")
            else:
                print(f"{short_id}. {path} [{format_size(size)}], download[{download_counter}]")

    def info(self, args : argparse.Namespace):
        name = args.name
        req_args = urlencode({"name": name, "type": "name", "user_token": self.cfg.get_cfg("UserToken")})
        resp = http.request_info(f"{self.cfg.SERVER}/detail?{req_args}")
        if resp is None:
            return False
        
        idd = resp["id"]
        name = resp["name"]
        path = resp["path"]
        descript = resp["descript"]
        size = resp["size"]
        raw_size = resp["raw_size"]
        num_files = resp["num_files"]
        user_name = resp["user_name"]
        is_directory = resp["is_directory"]
        create_time = resp["create_time"]
        update_time = resp["update_time"]
        delete_time = resp["delete_time"]
        permission  = resp["permission"]
        zipped = resp["zipped"]
        file_type = resp["file_type"]
        download_counter = resp["download_counter"]
        print(f"Found file {name}:")
        print(f"  id:          {idd}")
        print(f"  size:        {format_size(int(size))}")
        print(f"  rawsize:     {format_size(int(raw_size))}")
        print(f"  path:        {path}")
        print(f"  num_files:   {num_files}")
        print(f"  directory:   {is_directory}")
        print(f"  zipped:      {zipped}")
        print(f"  type:        {file_type}")
        print(f"  create_time: {create_time}")
        print(f"  update_time: {update_time}")
        print(f"  delete_time: {delete_time}")
        print(f"  user_name:   {user_name}")
        print(f"  permission:  {permission}")
        print(f"  download:    {download_counter}")
        print(f"  descript:    {descript}")

    def get(self, args : argparse.Namespace):
        name = args.name
        save = args.save
        no_unzip = args.no_unzip

        req_args = urlencode({"name": name, "type": "name", "user_token": self.cfg.get_cfg("UserToken")})
        resp = http.request_info(f"{self.cfg.SERVER}/detail?{req_args}")
        if resp is None:
            return False

        isdir = resp["is_directory"] == "True"
        zipped = resp["zipped"] == "True"
        do_unzip = True
        if not zipped or no_unzip:
            do_unzip = False

        local = save
        if os.path.isdir(save) or save[-1] == "/":
            os.makedirs(save, exist_ok=True)
            local = os.path.join(save, resp["name"])

        if not do_unzip:
            return http.request_file(f"{self.cfg.SERVER}/download?{req_args}", local, os.path.basename(local))

        with tempfile.TemporaryFile() as fp:
            if not http.request_file(f"{self.cfg.SERVER}/download?{req_args}", fp, resp["name"]):
                return False

            fp.seek(0)

            print("Unziping... please wait a moment.")
            zf = zipfile.ZipFile(fp, "r")
            members = zf.namelist()
            if isdir:
                pbar = tqdm(members)
                for zipinfo in pbar:
                    pbar.set_description(os.path.basename(zipinfo))
                    zf.extract(zipinfo, local)
                
                print(f"Save to: {local}")
                return True
            
            assert len(members) == 1, "Invalid members to unzip"
            with zf.open(members[0]) as source, \
                open(local, "wb") as target:
                shutil.copyfileobj(source, target)

            zf.close()
            print(f"Save to: {local}")
            return True

    def user(self, args : argparse.Namespace):
        print(f"Current user is: [{self.cfg.get_cfg('UserName')}]")

    def chperm(self, args : argparse.Namespace):
        req_args = urlencode({"path": args.path, "permission": args.permission, "user_token": self.cfg.get_cfg("UserToken")})
        resp = http.request_info(f"{self.cfg.SERVER}/change_permission?{req_args}")
        if resp is not None:
            print(f"Change the file [{args.path}] permission to {args.permission} success.")
            return True
        return False

    def login(self, args : argparse.Namespace):
        self.cfg.login()

    def run(self, args : argparse.Namespace):
        name = args.name
        remargs_string = " ".join(self.remargs)

        req_args = urlencode({"name": name, "type": "name", "user_token": self.cfg.get_cfg("UserToken")})
        resp = http.request_info(f"{self.cfg.SERVER}/detail?{req_args}")
        if resp is None:
            return False
        
        # isdir = resp["is_directory"] == "True"
        # zipped = resp["zipped"] == "True"
        file_type = resp["file_type"]

        if file_type not in ["bash", "python"]:
            print(f"This file type is unknow to run: {file_type}")
            return False

        data = http.request_rawdata(f"{self.cfg.SERVER}/download?{req_args}")
        if data is None:
            return False

        if file_type == "bash":
            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data)
                fp.seek(0)
                os.system(f"bash \"{fp.name}\" {remargs_string}")
        elif file_type == "python":
            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data)
                fp.seek(0)
                os.system(f"python3 \"{fp.name}\" {remargs_string}")

    def config(self, args : argparse.Namespace):
        if args.name == "user":
            value = args.value
            if not value.encode("utf-8").isalnum():
                print(f"An invalid username is entered. Only [a-zA-Z0-9] can be passed.")
                return False

            self.cfg.set_cfg("UserName", value)
            print(f"Set UserName to {value}")

    def delete(self, args : argparse.Namespace):
        path = args.path
        req_args = urlencode({"path": path, "user_name": self.cfg.get_cfg("UserName"), "user_token": self.cfg.get_cfg("UserToken")})
        if http.request_info(f"{self.cfg.SERVER}/delete?{req_args}") is not None:
            print(f"Delete file [{path}] success.")

    def put(self, args : argparse.Namespace):
        
        local = args.local
        file_type = args.type
        if not os.path.exists(local):
            print(f"File not found: {local}")
            return False

        remote = args.remote
        parent = self.cfg.get_cfg("UserName")
        if remote is None:
            remote = os.path.join(parent, os.path.basename(local))
        else:
            remote = os.path.join(parent, remote)

        local = local.replace("\\", "/")
        remote = remote.replace("\\", "/")
        permission = args.permission
        isdir = os.path.isdir(local)
        zipped = args.zip

        if local[-1] == "/":
            local = local[:-1]

        if remote[-1] == "/":
            remote = remote + os.path.basename(local)

        zip_compress = zipfile.ZIP_DEFLATED
        if not zipped:
            zip_compress = zipfile.ZIP_STORED

        if isdir:
            zipped = True
            if file_type != "archive":
                print(f"Invalid file type for: {file_type}, {local}")
                return False
            
        if file_type == "bash" or file_type == "python":
            print(f"set zipped = false When file type is {file_type}")
            zipped = False
        
        desc = args.desc
        files = [local]

        if isdir:
            ignore_file = os.path.join(local, ".emxignore")
            files = []
            for d, ds, fs in os.walk(local):
                for file in fs:
                    full_path = os.path.join(d, file)
                    if os.path.islink(full_path):
                        print(f"Ignore link file: {full_path}")
                        continue
                    
                    files.append(os.path.join(d, file))

        if zipped:
            with tempfile.TemporaryFile() as fp:
                zf = zipfile.ZipFile(fp, "w", compression=zip_compress)

                print(f"Compressing {len(files)} files with flag {zip_compress}... please wait a moment.")
                raw_size = 0

                if not isdir:
                    local = os.path.dirname(local)
                    if local == "":
                        local = "."

                if local[-1] != "/":
                    local += "/"

                for file in files:
                    name = file[len(local):]
                    raw_size += os.path.getsize(file)
                    zf.write(file, name)

                zf.close()
                new_size = fp.tell()
                print(f"raw_size = {format_size(raw_size)}, compress_size = {format_size(new_size)}, compress ratio: {abs(1 - new_size / raw_size) * 100:.2f} %")

                # if new_size >= 5 * 1024 * 1024:
                #     print(f"Over of limit for uploaded file size: {new_size / 1024 / 1024:.3f} MB, maximum = 5MB")
                #     return

                headers = {
                    "save": remote,
                    "file_size": str(new_size),
                    "raw_size": str(raw_size),
                    "descript": desc,
                    "is_directory": str(isdir),
                    "num_files": str(len(files)),
                    "zipped": str(zipped),
                    "file_type": file_type,
                    "user_name": self.cfg.get_cfg("UserName"),
                    "user_token": self.cfg.get_cfg("UserToken"),
                    "permission": permission
                }
                fp.seek(0)
                resp = http.upload_file(f"{self.cfg.SERVER}/upload", fp, headers, f"Upload: {remote}")
        else:
            size = os.path.getsize(local)
            # if size >= 5 * 1024 * 1024:
            #     print(f"Over of limit for uploaded file size: {size / 1024 / 1024:.3f} MB, maximum = 5MB")
            #     return

            headers = {
                "save": remote,
                "file_size": str(size),
                "raw_size": str(size),
                "descript": desc,
                "is_directory": str(isdir),
                "num_files": str(len(files)),
                "zipped": str(zipped),
                "file_type": file_type,
                "user_name": self.cfg.get_cfg("UserName"),
                "user_token": self.cfg.get_cfg("UserToken"),
                "permission": permission
            }
            resp = http.upload_file(f"{self.cfg.SERVER}/upload", local, headers, f"Upload: {remote}")

        if resp is not None:
            file_short_id = resp["id"]
            print(f"Complete to upload and you can use [file name: {remote} or short id: {file_short_id}] to view this file")

class Application:
    def __init__(self):
        self.cfg     = Config()
        self.actions = Actions(self)

    def run_with_command(self, args=None)->bool:
        
        if args is not None and isinstance(args, str):
            args = args.split(" ")
        elif args is None:
            args = sys.argv[1:]
        
        remargs = []
        if len(args) > 1 and args[0] == "run":
            run_name = args[1]
            remargs  = args[2:]
            args = ["run", run_name]

        cmd = Cmd(self.actions)
        c = cmd.add_cmd("get", "Get data from server")
        c.add_argument("name", type=str, help="repo name")
        c.add_argument("--id", action="store_true", help="use id to get")
        c.add_argument("--save", type=str, default=".", help="Save folder")
        c.add_argument("--no-unzip", action="store_true", help="Disable auto unzip")

        c = cmd.add_cmd("run", "Run script from server")
        c.add_argument("name", type=str, help="script name or id")

        c = cmd.add_cmd("put", "Put a file or directory to the remote server")
        c.add_argument("local", type=str, help="")
        c.add_argument("--remote", type=str, required=False, help="local 'whoami/local_name' if it is None")
        c.add_argument("--zip", action="store_true", help="Do zip file")
        c.add_argument("--desc", type=str, default="", help="Save folder")
        c.add_argument("--type", type=str, default="archive", help="File type, bash|python|archive")
        c.add_argument("--permission", type=str, default="private", help="set the file permission, options is: private, public, piazza")

        c = cmd.add_cmd("list", "Search the file by keyword.")
        c.add_argument("key", nargs="?", type=str, default="%", help="search name/path")
        c.add_argument("--count", type=int, default=20, help="show count")
        c.add_argument("--skip", type=int, default=0, help="show skip")

        c = cmd.add_cmd("cmds", "List all command lines.")
        c.add_argument("key", nargs="?", type=str, default="%", help="search name/path")
        c.add_argument("--count", type=int, default=20, help="show count")
        c.add_argument("--skip", type=int, default=0, help="show skip")
        
        c = cmd.add_cmd("delete", "Remove a file by path.")
        c.add_argument("path", type=str, help="file path.")

        c = cmd.add_cmd("chperm", "Change the remote file permission.")
        c.add_argument("path", type=str, help="file path.")
        c.add_argument("permission", type=str, help="new permission. private, public, and piazza are accepted.")

        c = cmd.add_cmd("config", "Config")
        c.add_argument("name", type=str, help="key")
        c.add_argument("value", type=str, help="value")

        c = cmd.add_cmd("login", "Login")
        c = cmd.add_cmd("user", "Print the current logined user name.")
        c = cmd.add_cmd("info", "Detail file")
        c.add_argument("name", type=str, help="search name")
        return cmd.run(args, remargs)