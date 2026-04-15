import os

# Build a portable path relative to this script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(SCRIPT_DIR, "tetx.txt")

# --- Read the file ---
try:
    with open(FILE_PATH, "r") as file_read:
        print("File in read mode - ")
        print(file_read.read())
except FileNotFoundError:
    print(f"Error: File not found at {FILE_PATH}")
except IOError as e:
    print(f"Error reading file: {e}")

# --- Write to the file (overwrites existing content) ---
try:
    with open(FILE_PATH, "w") as file_write:
        file_write.write(
            "THIS IS NOT LATIN, THIS IS RANDOM TEXT FROM THIS WEBSITE, "
            "https://loremipsum.io/generator/?n=9&t=p, "
            "Lorem ipsum dolor sit amet consectetur adipiscing elit. "
            "Quisque faucibus ex sapien vitae pellentesque sem placerat. "
            "In id cursus mi pretium tellus duis convallis. "
            "Tempus leo eu aenean sed diam urna tempor. "
            "Pulvinar vivamus fringilla lacus nec metus bibendum egestas. "
            "Iaculis massa nisl malesuada lacinia integer nunc posuere. "
            "Ut hendrerit semper vel class aptent taciti sociosqu. "
            "Ad litora torquent per conubia nostra inceptos himenaeos."
        )
        file_write.write("FILE IN WRITE MODE --")
except IOError as e:
    print(f"Error writing to file: {e}")

# --- Append to the file ---
try:
    with open(FILE_PATH, "a") as file_append:
        file_append.write(
            "THIS IS NOT LATIN, THIS IS RANDOM TEXT FROM THIS WEBSITE, "
            "https://loremipsum.io/generator/?n=9999999999999999999999999999999999999999999999&t=p, "
            "Lorem ipsum dolor sit amet consectetur adipiscing elit. "
            "Quisque faucibus ex sapien vitae pellentesque sem placerat. "
            "In id cursus mi pretium tellus duis convallis. "
            "Tempus leo eu aenean sed diam urna tempor. "
            "Pulvinar vivamus fringilla lacus nec metus bibendum egestas. "
            "Iaculis massa nisl malesuada lacinia integer nunc posuere. "
            "Ut hendrerit semper vel class aptent taciti sociosqu. "
            "Ad litora torquent per conubia nostra inceptos himenaeos."
        )
        file_append.write("FILE IN append MODE --")
except IOError as e:
    print(f"Error appending to file: {e}")
