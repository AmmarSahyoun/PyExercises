# parrot = 'Norwegian Blue'
#
# for character in parrot:
#     print(character)
# print('Hej då')

number ='9,233;372:036 854, 776:807'
seperators = number[1::4]

values = ''.join(char if char not in seperators else ' ' for char in number).split()
print()
print([int(val) for val in values])