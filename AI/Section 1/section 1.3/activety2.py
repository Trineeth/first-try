idea = int(input())
file = open('C:/Users/trine/OneDrive/Documents/python class/AI/Section 1/section 1.3/textt.txt', 'r')
print(file.read())
file.close()

file = open('C:/Users/trine/OneDrive/Documents/python class/AI/Section 1/section 1.3/textt.txt', 'r')
print("\n Read in parts\n")
print(file.read(idea))
file.close()

file = open('C:/Users/trine/OneDrive/Documents/python class/AI/Section 1/section 1.3/textt.txt', 'w')
file.write(" Hi! I am Tingu and 11 years old")
file.close()

file = open('C:/Users/trine/OneDrive/Documents/python class/AI/Section 1/section 1.3/textt.txt', 'a')
file.write(" Hi! I am Tingu and 11 years old")
file.close()