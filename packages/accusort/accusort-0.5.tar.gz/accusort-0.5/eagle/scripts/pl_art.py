from art import text2art
import os
LOG_FILE = "log.txt"

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to banner.txt
banner_file = os.path.join(script_dir, 'banner.txt')

BANNER_FILE = banner_file


def print_colored_text(text, color):
    # ANSI color escape codes
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m",
    }
    color_code = colors.get(color.lower(), "")

    # Print colored text
    print(f"{color_code}{text}{colors['reset']}")


def print_eagle():
    # Print colored ASCII art of an eagle
    eagle = text2art("Eagle")
    print_colored_text(eagle, "blue")

    # Print the content of banner.txt if it exists
    try:
        with open(BANNER_FILE, "r") as banner_file:
            banner_content = banner_file.read()
            print_colored_text(banner_content, "blue")
    except FileNotFoundError:
        print(f"Banner file '{BANNER_FILE}' not found.")
