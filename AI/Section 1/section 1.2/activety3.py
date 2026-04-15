import os

# Build a portable path relative to this script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(SCRIPT_DIR, "tetx.txt")

# --- Append user input to the file ---
user_text = input("Enter text to append to the file: ")

try:
    with open(FILE_PATH, "a") as file_append:
        file_append.write(user_text)
        print("Text appended successfully.")
except IOError as e:
    print(f"Error appending to file: {e}")
