# age = int(input('Hut gammal är du?'))
#
# if age >= 18 and  age <= 65:
#     print('välkommen till Arbetsförmedlingen')
# else:
#     print('Du behöver inte arbeta!')
#
# print('Ha en bra dag')
# print('-'*80)

# day = 'lördag'
# temp = 9
# raining = True
#
# print('idag är det {} och det är {} grader'.format(day, temp))
#
# if day == ('tis' or temp > 6) and not raining:
#     print('Gå till straden')
# else:
#     print('studera python')

# if 1:
#     print('True')
# else:
#     print('False')

# name = input('var vänlig ange ditt name')
# if name:
#     print('Hejsan, {}'.format(name))
# else:
#     print('välkomen du namelöse')
#
# print(len(name))

import random
highest_limit = 100
answer = random.randint(1, highest_limit)
print(answer) # REMOVE after testing

print('var vänlig gissa ')
guess = int(input())

if guess == answer:
    print('Du gissa rättttttt på första gång ')
else:
    if guess < answer:
        print('var vänlig gissa högre')
    else:
        print('var vänlig gissa lägre')
    guess = int(input())
    if guess == answer:
        print('Grattis, du är rätt')
    else:
        print('Tyvärr, du är fel')
print(' Tack för att du spelade')
