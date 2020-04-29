# parrot = 'Norwegian Blue'
#
# for character in parrot:
#     print(character)
# print('Hej då')

number = '9,233;372:036 854, 776:807'
seperators = number[1::4]

values = ''.join(char if char not in seperators else ' ' for char in number).split()
print()
print([int(val) for val in values])

# answer = 5
#
# print('Var vänlig ange ett tal mellan 1 och 10: ')
# guess = int(input())
#
#
# if guess != answer: # hur ändrar man koden om första villkoret ändrat till if guess == answer
#     if guess < answer:
#         print("Var vänlig gässa högre")
#     else:
#         print('Var vänlig gissa lägre')
#     guess = int(input())
#     if guess == answer:
#         print('Grattis, di gissade rätt')
#     else:
#         print('Tyvärr du har gissat fel')
# else:
#     print('Du gissade rätt på första försöket')
#
#
# print('Tack för att du spelade')
# if guess < answer:
#     print("Var vänlig gässa högre")
#     guess = int(input())
#     if guess == answer:
#         print('Grattis, di gissade rätt')
# elif guess > answer:
#     print('Var vänlig gissa lägre')
#     guess = int(input())
#     if guess == answer:
#         print('Grattis, du gissade rätt')
# else:
# #     print('Du gissade rätt på första försöket')
