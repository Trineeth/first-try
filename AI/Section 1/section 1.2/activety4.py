import os

# Build a portable path relative to this script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(SCRIPT_DIR, "tetx.txt")

# --- Count non-empty lines in the file ---
try:
    with open(FILE_PATH, "r") as file:
        content = file.read()
        lines = content.split("\n")
        counter = sum(1 for line in lines if line)
        print(counter)
except FileNotFoundError:
    print(f"Error: File not found at {FILE_PATH}")
except IOError as e:
    print(f"Error reading file: {e}")
