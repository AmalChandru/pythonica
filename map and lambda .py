# We are going to check a letter in the list elements
list = ["Zorba","The","Greek","Nikos", "kazantzakis"]
# map(fuction,iterable)
a = map(lambda s:(True) if "e" in s else (False),list)
print(a)


