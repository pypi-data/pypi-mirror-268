import argparse
import os
import pyperclip

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
    print("Content copied to clipboard.")

def copy_folder_content(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                pyperclip.copy(content)
                print(f"Content of {filename} copied to clipboard.")

def main():
    parser = argparse.ArgumentParser(description='Command-line tool for file management and copying to clipboard.')
    parser.add_argument('command', choices=['create', 'read', 'copy', 'ls', 'copy_folder', 'new_command'], help='Command to execute')
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
    elif args.command == 'ls':
        files_list = list_files()
        print("Files in current directory:")
        print(files_list)
    elif args.command == 'copy_folder':
        copy_folder_content(args.filename)
    elif args.command == 'new_command':
        # Implement functionality for your new command here
        print("New command executed.")

if __name__ == "__main__":
    main()
