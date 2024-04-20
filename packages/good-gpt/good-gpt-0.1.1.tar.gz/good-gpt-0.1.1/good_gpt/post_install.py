import os
import sys
import subprocess

def add_to_path_on_unix(path):
    shell_profile = "~/.bashrc"  # Default to bash
    if 'ZSH_VERSION' in os.environ:
        shell_profile = "~/.zshrc"
    elif 'FISH_VERSION' in os.environ:
        shell_profile = "~/.config/fish/config.fish"

    # Resolving the path
    path = os.path.expanduser(path)

    # Command to append to the shell configuration file
    export_cmd = f'export PATH="$PATH:{path}"\n'

    if 'fish' in shell_profile:
        export_cmd = f'set -gx PATH $PATH {path}\n'

    # Checking if the path is already in PATH
    if path not in os.getenv('PATH', '').split(':'):
        # Writing command to the shell configuration file
        with open(os.path.expanduser(shell_profile), 'a') as file:
            file.write(export_cmd)
        print(f"Added {path} to PATH in {shell_profile}")
    else:
        print(f"{path} is already in the PATH in {shell_profile}. Nothing to do.")

def add_to_path_on_windows(path):
    # Getting current user PATH environment variable value
    user_path = os.getenv('PATH')

    # Appending the new path if it's not already in the PATH
    if path not in user_path:
        new_user_path = user_path + ';' + path
        subprocess.run(['setx', 'PATH', new_user_path], check=True)
        print(f"Added {path} to PATH for Windows")
    else:
        print(f"{path} is already in the PATH for Windows. Nothing to do.")

def main():
    # Depending on the OS, we find the default installation path of Python Scripts or binaries
    if os.name == "posix":
        default_path = os.path.expanduser("~/.local/bin")
        add_to_path_on_unix(default_path)
    elif os.name == "nt":
        python_executable = sys.executable
        scripts_path = os.path.join(os.path.dirname(python_executable), 'Scripts')
        add_to_path_on_windows(scripts_path)
    else:
        print("Unsupported Operating System.")

if __name__ == "__main__":
    main()