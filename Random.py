# import random
# highest_limit = 100
# answer = random.randint(1, highest_limit)
# print(answer) # REMOVE after testing
#
# print('var vänlig gissa ')
# guess = int(input())
#
# if guess == answer:
#     print('Du gissa rättttttt på första gång ')
# else:
#     if guess < answer:
#         print('var vänlig gissa högre')
#     else:
#         print('var vänlig gissa lägre')
#     guess = int(input())
#     if guess == answer:
#         print('Grattis, du är rätt')
#     else:
#         print('Tyvärr, du är fel')
# print(' Tack för att du spelade')

low = 1
high = 1000
guesses = 1
print('think about  a number between {} and {}'.format(low, high))
print('....')
while True:
    guess = low + (high - low) // 2

    choose = input('I guess your No is {} is it correct[C],lower[l] or higher[h]'.format(guess)).casefold()

    if choose == 'h':
        low = guess + 1
    elif choose == 'l':
        high = guess - 1
    elif choose == 'c':
        print('i guessed your number {} in {} times'.format(guess, guesses))
        guesses += 1
        break

    guesses += 1
print(' thank you for trying our game ')