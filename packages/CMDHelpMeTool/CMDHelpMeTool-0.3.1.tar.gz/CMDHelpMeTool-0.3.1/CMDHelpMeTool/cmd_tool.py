import argparse
import pyperclip
import experiments  # Import the experiments module

def copy_variable_to_clipboard(variable_name):
    # Get the variable value based on the variable name
    variable = getattr(experiments, variable_name, None)
    if variable is not None:
        pyperclip.copy(variable)
        print(f"Content of '{variable_name}' copied to clipboard.")
    else:
        print(f"Variable '{variable_name}' not found.")

def main():
    parser = argparse.ArgumentParser(description='Command-line tool for copying variable content to clipboard.')
    parser.add_argument('command', choices=['copy_experiment'], help='Command to execute')
    parser.add_argument('variable_name', help='Name of the variable to copy')

    args = parser.parse_args()

    if args.command == 'copy_experiment':
        copy_variable_to_clipboard(args.variable_name)

if __name__ == "__main__":
    main()
