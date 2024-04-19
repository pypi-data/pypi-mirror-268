import subprocess
import importlib
import sys
import os


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def print_error(message):
    """
    Print an error message.
    """
    print(f"[\033[91m-\033[0m] {message}")


def print_success(message):
    """
    Print a success message.
    """
    print(f"[\033[92m+\033[0m] {message}")


def print_warning(message):
    """
    Print a warning message.
    """
    print(f"[\033[93m!\033[0m] {message}")


def package(package):
    """
    Execute command to download any dependencie/s
    """
    subprocess.check_call([sys.executable, "-m", "pip", "install", f"{package}"])


def install(package):
    """
    Install all need dependencie/s
    """
    try:
        importlib.util.find_spec(package)
    except ImportError:
        print(f"{package} is not installed. installing...")
        package(package)
