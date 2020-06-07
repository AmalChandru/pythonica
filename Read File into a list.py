# Program to read a file to a list
# print([expression context])
# pythonic way
print([lines.strip() for lines in open("code.py")])
# Noob way
code = open("code.py")
lines =[]
for lines in code:
    lines.append(lines.strip())
print(lines)

