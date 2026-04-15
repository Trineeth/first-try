import os

file_path = os.path.join(os.path.dirname(__file__), 'tetx.txt')

MAX_INPUT_LENGTH = 10000

user_input = input("")
if len(user_input) > MAX_INPUT_LENGTH:
    print(f"Input too long. Maximum {MAX_INPUT_LENGTH} characters allowed.")
else:
    with open(file_path, 'a') as file_append:
        file_append.write(user_input)
