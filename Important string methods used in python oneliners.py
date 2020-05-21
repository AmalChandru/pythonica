# Important string methods used in python oneliners
print("ZoRBa THe GREEk".lower())
# Lowercase
# zorba the greek
print("ZoRBa THe GREEk".upper())
# Uppercase
# ZORBA THE GREEK
print("Zorba the Greek".startswith("Zorba"))
# Returns bool by checking string's prefix
# True
print("Zorba the Greek".endswith("Greek"))
# Returns bool by checking string's suffix
# True
print("another".find("other"))
# Returns matching index
# 2
print("cheatch".replace("ch","m",1))
# Replaces all occurrences of the first by the second argument
# meatch
print("cheatch".replace("ch","m",2))
# meatm
print('$'.join(["F","G","H"]))
# Glues all elements in list using seperator string
# F$G$H
print(len("Pythonics!"))
# String length
# 10
print("ea"in"earth")
# Contains
# True