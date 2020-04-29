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

print('+++++++++++++list+++++++++++')
newList = ["one", "car", "two", "one", 9, 100.5, False]
print(newList)  # whole list
print(newList[0], newList[-1])  # first and last
print('+++++++++ slicing +++++++++++')
print(newList[1:4])
print(newList[::3])  #start end step


newList[1] = "five"
print(newList)

newList[1:4] = ["buss", 2, 1]
print(newList)

newList[1:3] = ["buss", 2, 1]
print(newList)

print('========append=========')
newList.append("Ammar")
print(newList)

newList.append(myList)
print(newList)

print('+++++++extend++++++++')
k = [1, 3, 5, 7]
l = ["a", "m", "z"]
o = ["one", "two"]
k.extend(l)
k.extend(o)
print(k)
