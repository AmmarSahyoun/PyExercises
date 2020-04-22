# calculate age
# age = input('please write you age: ').strip()
# unit = input("Choose time unit: [1]Months, [2]Weeks, [3]Days: ").strip().lower()
#
#
# months = int(age) * 12
# weeks = months * 4
# days = int(age) * 365
#
# if unit == 'months' or 1 :
#     # print("you choose the unit months")
#     print(f"\nyou lived for {months:,} Months.")
#
# elif unit == 'weeks' or 2:
#     # print("you choose the unit Weeks")
#     print(f"\nyou lived for {weeks:,} Weeks.")
#
# elif unit == 'days' or 3:
#     # print("you choose the unit Days")
#    print(f"\nyou lived for {months:,} Days.")

# ====== create  a file and overwrite it===========

fh = open('demo.txt', 'w')  # create a file and overwrite it
fh.write(' this is my first file creation in python\n')

for i in range(9):
    fh.write("this is line No %d\n " % (i + 1))
fh.close()

fh = open('demo.txt', 'a')
try:
    for i in range(3):
        fh.write("add text to the file by using append'a' %d\n " % (i + 1))
finally:  # called in exceptions cases
    fh.close()
print('creation demo file was done successfully')

with open('demo2.txt', 'w') as fh2:
    for i in range(2):
        fh2.write('this is a shorter code, line No %d\n' % (i + 1))
print('creation demo2 file was done successfully')

print('creation demo3 C:\\Users\\Ammar\\Desktop \n done successfully!')
with open('C:\\Users\\Ammar\\Desktop\\demo3.txt', 'w') as fh3:
    for i in range(5):
        fh3.write('\n this files created by Python, line No %d\n' % (i + 1))
