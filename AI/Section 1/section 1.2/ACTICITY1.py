import os

file_path = os.path.join(os.path.dirname(__file__), 'tetx.txt')

with open(file_path) as file:
    print(file.read())
