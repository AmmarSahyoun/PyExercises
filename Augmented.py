# x = 25
# print(x)
# # x = x + 5
# x += 5
# print(x)
# augmented_part = 5
# x += augmented_part
# # x = x + augmented_part
# print(x)

# x = 25
# print(x)
#
# x += 3
# print(x)
#
# x -= 8
# print(x)
#
# x *= 5
# print(x)
#
# x //= 4
# print(x)

low = 1
high = 1000

print('tänk på ett tal mellan {} och {}'.format(low, high))
input('tryck ENTER för börja')

guesses = 1
while True:
    guess = low + (high - low) // 2
    high_low = input('jag gissar{} ska jag gissa l LOWER'
                     'eller h högre och C om jag correct'.format(guess)).casefold()

    if high_low == 'h':
        low = guess +1
    elif high_low == 'l':
        high = guess - 1
    elif high_low == 'c':
        print('gissade rätt på {} antal'.format(guesses))
        break
    else :
        print(' choose h,l eller c')

    guesses += 1

print('slut')
