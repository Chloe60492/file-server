# cli/main.py
import cmd
from cli import utils

class FileServerCLI(cmd.Cmd):
    intro = "Welcome to the File Server CLI. Type help or ? to list commands.\n"
    prompt = "(file-server) "

    def do_upload(self, arg):
        "Upload a file to the server: upload <file_path>"
        if not arg:
            print("Usage: upload <file_path>")
            return
        result = utils.upload_file(arg.strip())
        print(result)

    def do_download(self, arg):
        "Download a file from the server: download <file_name>"
        if not arg:
            print("Usage: download <file_name>")
            return
        result = utils.download_file(arg.strip())
        print(result)

    def do_list(self, arg):
        "List all files stored on the server"
        result = utils.list_files()
        print(result)

    def do_delete(self, arg):
        "Delete a file from the server: delete <file_name>"
        if not arg:
            print("Usage: delete <file_name>")
            return
        result = utils.delete_file(arg.strip())
        print(result)

    def do_exit(self, arg):
        "Exit the CLI"
        print("Exiting...")
        return True

    def do_help(self, arg):
        if arg:
            try:
                func = getattr(self, f'do_{arg}')
                print(func.__doc__)
            except AttributeError:
                print(f"No help found for '{arg}'")
        else:
            super().do_help(arg)

    def emptyline(self):
        pass  # Ignore empty inputs instead of repeating the last command

if __name__ == '__main__':
    FileServerCLI().cmdloop()
