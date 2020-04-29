# a = 0
# b = 'Ammaro'
# while a < 6:
#     print(b[a])
#     a += 1
# else:    # when the true become false
#     print(' loop is done')

# for i in range (10):
#     print('i is now {}'.format(i))

# i = 0
# while i < 10:   #
#     print(' i is now {}'.format(i))
#     i += 2

# i = 0
# while True:
#     print(' i is now {}'.format(i))
#     i += 1
#     if i ==7:
#         break
# print(' vi kom ut trots allt')

available_direction = ['north', 'south', 'east', 'west']
chosen_direction = ''
while chosen_direction not in available_direction:  # true
    chosen_direction = input('Välj en riktning: ')
    if chosen_direction.casefold() == 'quit':
        print('spelat är slut!')
        break

print('Äntligen ute!')
# casefold .. make everythin lower_case
