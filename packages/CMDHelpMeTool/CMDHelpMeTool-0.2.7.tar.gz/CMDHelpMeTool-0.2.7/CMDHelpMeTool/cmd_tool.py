import argparse
import pyperclip

exp1 = "If you can't upload your project's release to PyPI because you're hitting the upload file size limit, we can sometimes increase your limit. Make sure you've uploaded at least one release for the project that's under the limit (a developmental release version number is fine). Then, file an issue and tell us:\n\nA link to your project on PyPI (or Test PyPI)\nThe size of your release, in megabytes\nWhich index/indexes you need the increase for (PyPI, Test PyPI, or both)\nA brief description of your project, including the reason for the additional size."

def create_file(filename):
    with open(filename, 'w') as file:
        file.write('Sample text in ' + filename)

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File '{filename}' not found."

def list_files():
    files = os.listdir('.')
    return '\n'.join(files)

def copy_to_clipboard(text):
    pyperclip.copy(text)

def copy_variable_to_clipboard(variable):
    pyperclip.copy(variable)
    print("Variable content copied to clipboard.")

def main():
    parser = argparse.ArgumentParser(description='Command-line tool for file management and copying to clipboard.')
    parser.add_argument('command', choices=['create', 'read', 'copy', 'ls', 'copy_variable', 'new_command'], help='Command to execute')
    parser.add_argument('filename', nargs='?', help='File name')

    args = parser.parse_args()

    if args.command == 'create':
        create_file(args.filename)
        print(f"File '{args.filename}' created successfully.")
    elif args.command == 'read':
        content = read_file(args.filename)
        print(content)
    elif args.command == 'copy':
        content = read_file(args.filename)
        copy_to_clipboard(content)
        print("File content copied to clipboard.")
    elif args.command == 'ls':
        files_list = list_files()
        print("Files in current directory:")
        print(files_list)
    elif args.command == 'copy_variable':
        copy_variable_to_clipboard(exp1)
    elif args.command == 'new_command':
        # Implement functionality for your new command here
        print("New command executed.")

if __name__ == "__main__":
    main()
