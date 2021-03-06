x = ['one', 1, 9, 100.5, False, 'Ammar', 'My', 'ammar', 'is', 'Ammar', "tree"]
x.remove("Ammar")  # remove first element just
print(x)

# sort
y = [45, 975, 1, 65, 21, 4, 2, 5]
y.sort()
print(y)

t = ['f', 't', 'i', 'a']
t.sort(reverse=True)
print(t)

# clear
a = [1, 4, 5, 6, 7]  # main list
a.clear()
print(a)

a = [1, 4, 5, 6, 7]
s = a.copy()  # copied list
s.append(666)
print(s)

# count
print(x.count("Ammar"))  # 1: after we remove the first Ammar

# index
print(x.index("ammar"))

# insert
x.insert(0, "AAAA")
x.insert(-1, "ZZZZ")
print(x)

# pop
g = [1, 2, 3, 4, 8, 9, 'a', 'r']
print(g.pop(-3))

# tuples
myTuple1 = ("Ammar", "Anna")
myTuple2 = (5,4,6,8,12,1,979)
print(myTuple1)

print(myTuple2[-1])
string  = "Lubna"
myList = [2,5]
myTuple = ("El", "deres")

print(string * 5)
print(myList * 5)
print(myTuple * 5)

# set has no indexes, immutable data only
mySet = {"Ammar", "Tonny", 15}
print(mySet)
print(mySet)