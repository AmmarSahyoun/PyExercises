# Index ( SubString, Start, End)
a = "I Love Programming"
print(a.index("P"))
print(a.index("P", 0, 10))

print("m located in the index No:", a.find("m"))

# rjust(width, fill char)

c = "Ammar"
print(c.ljust(10), "#")
print(c.rjust(9), "#")

# splitlines

e = """ First line
Second Line
Third Line """

print(e.splitlines())
print(type(e.splitlines()))

g = "Hello\tWorld\tthis\tis\tAmmar"
print(g)
print(g.expandtabs(15))

f = "My Name Is Ammar"
print(f.istitle())
print(f.islower())

# alphabetical
l = "AFHGELIFHWjdk5sjlieAKF23JDYWUEWHjdhgGGL45SKFJLUjfgfduihgui553oh"
if print(l.isalnum()) == False:
    print("not an alphabetical or numrical phrase ")
else:
    print(" it contains numeric and alphabetical letters without spaces")
