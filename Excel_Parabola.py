# def parabola(x):
#     y = x ** 2
#     return y
#
#
# for value in range(-5, 6):
#     squared = parabola(value)
#     print('{} i kvadrat är {:2d}'.format(value, squared))
# --------------------------------------------------------------------
# low = 1
# high = 1000
#
# print('tänk på ett tal mellan {} och {}'.format(low, high))
# input('tryck ENTER för börja')
#
# guesses = 1
# while True:
#     guess = low + (high - low) // 2
#     high_low = input('jag gissar{} ska jag gissa l LOWER'
#                      'eller h högre och C om jag correct'.format(guess)).casefold()
#
#     if high_low == 'h':
#         low = guess + 1
#     elif high_low == 'l':
#         high = guess - 1
#     elif high_low == 'c':
#         print('gissade rätt på {} antal'.format(guesses))
#         break
#     else:
#         print(' choose h,l eller c')
#
#     guesses += 1
#
# print('slut')
# ---------------------------------------
low = 8
high = 50
counter = 1
print('guess a number between {} and {}:'.format(low, high))
input('press Enter to start the game:')
while True:
    sma = low + (high - low) // 2
    inp = input('is your number {}?, enter[c]Correct, [l]lower, [h]higher'.format(sma).lower())
    if inp =='h':
        low = sma

    if inp == 'l':
        high = sma

    elif inp == 'c':
        print('I guessed your number after {} times'.format(counter))
        break
    counter += 1
print('Game end')
