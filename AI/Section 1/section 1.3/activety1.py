import os

file_path = os.path.join(os.path.dirname(__file__), 'textt.txt')

try:
    idea = int(input())
except ValueError:
    print("Please enter a valid number.")
    exit()

with open(file_path, 'r') as file:
    print(file.read())

with open(file_path, 'r') as file:
    print("\n Read in parts\n")
    print(file.read(idea))

with open(file_path, 'a') as file:
    file.write(" Hi! I am a student and learning Python")
