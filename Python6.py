age = 44
country = "Sweden"
rank = 10
print(age > 16 and country == "Sweden" and rank > 0)
print(age > 16 or country == "Syria" or rank > 0)
x = 25
y = 2
z = x + y
print("\n result:", z)
x //= y  # add to x the value of y
print(x)
print("=" * 50)
print(100 == 100)  # true
print(100 <= 200)  # true
print(100 == 100.00)  # true
print("+tuple+" * 10)
c = "Ammar"
d = [1, 2, 3, 4, 5]
e = {"A", "B", "c"}  # set are unOrdered
f = {"A": 1, "B": 2}
print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))
print("=LIST=" * 10)
d = (1, 2, 3, 4, 5)
print(list(c))
print(list(d))
print(list(e))
print(list(f))
print("=SET=" * 10)
e = ["A", "B", "c"]
print(set(c))
print(set(d))
print(set(e))
print(set(f))
print("=Dict=" * 10)
d = (("A", 1), ("B", 2), ("C", 3))  # nested tuple
#  print(dict(c))
print(dict(d))
e = [["one", 1], ["Two", 2], ["three", 3]]
print(dict(e))
f = {{1, "one"}, {2, "two"}}
print(dict(f))  # ((( unhashable type: 'set')))

fName = input("Enter your first name:")
lName = input("Enter your last name:")
fName = fName.strip().capitalize()
lName = lName.strip().capitalize()
email = input("Enter your email:")
print(f"Hello {fName} {lName} and welcome")
print("your Domain is:", email[email.index("@")+1:])
