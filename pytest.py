import os
import subprocess
import sys
import venv
from tqdm import tqdm


def create_virtualenv(base_dir, venv_name):
    """Creates a virtual environment in the specified base directory if it doesn't exist."""
    venv_path = os.path.join(base_dir, venv_name)
    if not os.path.exists(venv_path):
        print(f"Creating virtual environment at {venv_path}...")
        venv.create(venv_path, with_pip=True)
    else:
        print(f"Virtual environment already exists at {venv_path}.")
    return venv_path


def install_dependencies(venv_path):
    """Installs all dependencies listed in requirements.txt in the virtual environment with a progress bar."""
    print("Installing dependencies from requirements.txt in the virtual environment...")
    if sys.platform == 'win32':
        pip_executable = os.path.join(venv_path, 'Scripts', 'pip')
    else:
        pip_executable = os.path.join(venv_path, 'bin', 'pip')

    requirements_file = 'requirements.txt'
    if os.path.exists(requirements_file):
        with open(requirements_file, 'r') as f:
            lines = f.readlines()
            total_packages = len(lines)

        with tqdm(total=total_packages, desc="Installing dependencies", unit="pkg") as pbar:
            for line in lines:
                package = line.strip()
                if package:
                    subprocess.check_call([pip_executable, 'install', package])
                    pbar.update(1)
    else:
        print(f"No requirements.txt file found in the current directory.")


def activate_and_run_server(venv_path, name):
    """Activates the virtual environment and runs the Django server."""
    print("Activating virtual environment and running the server...")
    if sys.platform == 'win32':
        activate_script = os.path.join(venv_path, 'Scripts', 'activate.bat')
        command = f'cmd /k "{activate_script} && python manage.py runserver"'
    else:
        activate_script = os.path.join(venv_path, 'bin', 'activate')
        command = f'/bin/bash -c "source {activate_script} && python manage.py runserver"'

    print(f'Welcome to Django Mr/Ms {name}')
    subprocess.call(command, shell=True)


if __name__ == "__main__":
    base_dir = os.getcwd()  # Use the current directory where the terminal is open
    venv_name = 'myenv'
    name = 'Dikshant Katwal'  # Replace this with the actual name or get it from input

    venv_path = create_virtualenv(base_dir, venv_name)
    install_dependencies(venv_path)
    activate_and_run_server(venv_path, name)