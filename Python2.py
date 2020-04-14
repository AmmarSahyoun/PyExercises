# join
myList = ["My", "name", "is", "Ammar"]
print("-".join(myList))
print(type("-".join(myList)))

# placeholder %
name = "Ammar"
age = 44
rank = 10
print("my name is:" + name)
print("my name is: %s and my age is: %d and my rank is: %d" % (name, age, rank))
print()
# rearrangement
a, b, c = "first", "second", "third"
print("Sequence is {} {} {}".format(a, b, c))
print("Sequence is {1} {0} {2}".format(a, b, c))
print("Sequence is {} {} {}".format(c, a, b))
print()
# format
print("my name is : {name} and my age is :{age}")
print(f"my name is : {name} and my age is :{age}")

# numbers

