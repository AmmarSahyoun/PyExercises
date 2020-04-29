# shopping_list = ['dator','mus','musmata','mus','tangentbord']
shopping_list = []

# shopping_list.append('dator')
# shopping_list.append('mus')
# shopping_list.append('musmata')
# shopping_list.append('monitor')
# shopping_list.append('tangentbord')
# shopping_list.append('kabel')

while True:

    item = input('Enter item title to add or[q] to quit: ')
    if item == 'q':
        break
    else:
        shopping_list.append(item)

for goods in sorted(shopping_list):
    print(goods)

# item_to_find = 'kabel'
# found = None
#
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found = index
#         break
#
# if found:
#     print('vårat sökta föremål fanns på position {}'.format(found))
# else:
#     print('föremålet fanns inte i listan')
