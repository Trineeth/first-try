import os

file_path = os.path.join(os.path.dirname(__file__), 'tetx.txt')
counter = 0

with open(file_path, 'r') as file:
    content = file.read()
    Colist = content.split("\n")

    for i in Colist:
        if i:
            counter += 1
print(counter)
