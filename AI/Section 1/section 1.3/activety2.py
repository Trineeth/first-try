import os

# Build a portable path relative to this script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(SCRIPT_DIR, "textt.txt")

# --- Read the entire file ---
try:
    with open(FILE_PATH, "r") as file:
        print(file.read())
except FileNotFoundError:
    print(f"Error: File not found at {FILE_PATH}")
except IOError as e:
    print(f"Error reading file: {e}")

# --- Read a specific number of characters ---
try:
    idea = int(input("Enter the number of characters to read: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
else:
    try:
        with open(FILE_PATH, "r") as file:
            print("\n Read in parts\n")
            print(file.read(idea))
    except FileNotFoundError:
        print(f"Error: File not found at {FILE_PATH}")
    except IOError as e:
        print(f"Error reading file: {e}")

# --- Write to the file (overwrites existing content) ---
try:
    with open(FILE_PATH, "w") as file:
        file.write(" Hi! I am Tingu and 11 years old")
except IOError as e:
    print(f"Error writing to file: {e}")

# --- Append to the file ---
try:
    with open(FILE_PATH, "a") as file:
        file.write(" Hi! I am Tingu and 11 years old")
except IOError as e:
    print(f"Error appending to file: {e}")
