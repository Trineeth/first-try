file = open('C:/Users/trine/OneDrive/Documents/python class/AI/Section 2/tetx.txt', 'r')
counter = 0

content = file.read()
Colist = content.split("\n")

for i in Colist:
    if i:
        counter += 1
print(counter)