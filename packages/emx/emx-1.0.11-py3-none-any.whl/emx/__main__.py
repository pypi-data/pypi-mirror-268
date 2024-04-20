
import emx

def main():
    app = emx.Application()
    app.run_with_command()

def run():
    app = emx.Application()

    import sys
    args = ["run"] + sys.argv[1:]
    app.run_with_command(args)

if __name__ == "__main__":
    main()