# myFavouriteWebs = []
# maximumWebs = 5
#
# while maximumWebs > 0:
#     web = input('website name without https://')
#     myFavouriteWebs.append('https://{}'.format(web.strip().lower()))
#     maximumWebs -= 1
#     print('website added, {} places left'.format(maximumWebs))
#     print(myFavouriteWebs)
#
# else:
#     print('the list is full, you cannot add more')
#
# if len(myFavouriteWebs) > 0:
#     myFavouriteWebs.sort()
#     index = 0
#     while index < len(myFavouriteWebs):
#         print(myFavouriteWebs[index])
#         index += 1

# tries = 4
# mainPassword = 's'
# inputPassword = input('write your password')
# while inputPassword != mainPassword:
#     tries -= 1
#     # in case of conditional print we need to use  prentathes " not single '
#     print(f"wrong password, {'Last' if tries == 1 else tries} chance left")
#     inputPassword = input('write your password')
#     if tries == 1:
#         print(' you entered wrong password 4 times')
#         break
#         print('hhhhhhhhhhhhhfffffffffffffffffffffffffffffff')
#
# else:
#     print('correct password')

# myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for number in myNumbers:
#     #print(number * 17)
#     if number % 2 == 0:
#         print('the number {} is Even'.format(number))
#     else:
#         print('the number {} is Odd'.format(number))
# print('+++ the loop is finished')


# myRange = range(1, 100)  # create num from 1 to 1000
# for number in myRange:
#     print(number)
