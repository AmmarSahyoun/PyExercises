# =======READ============
fh = open('demo.txt', 'r')
# print(fh.read()) # this function will prevent readlines function
# print(fh.readline(4))  # read first 4 char
# print(fh.readline())  # consider the rest in the next line
# print(fh.readline())
# print(fh.readline())
# fh.close()

# with open('demo2.txt', 'r') as fh2:
#     print('convert txt file to list\n', fh2.readlines())  # convert the file to list
#     print(fh2.readlines()[2])

fh2 = open('demo2.txt', 'r')
for line in fh2:
    print(line)
    print(len(line))  # length of each line
    print(line.split(' '))  # list of every word in every line
    print(len(line.split(' ')))  # number of words in each line
    print("-------------------------\n")
# if the fh file handler read the whole file it will not read again
att