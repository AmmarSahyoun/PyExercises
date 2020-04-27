# for i in range(0, 10, 2):
#     print(' i is now {}'.format(i))


# for i in range(1, 7):
#     for j in range(1, 7):
#         print('{:2d}'.format(i+j), end=" ")  # :5d
#     print()


# for i in range(1, 3):
#     for j in range(1, 3):
#         for k in range(1, 3):
#             print('{}, {}, {}'.format(i,j,k))

# shoppin_list = ['dator', 'monitor', 'musmatta', 'mus', 'tangentbord']
#
# for item in shoppin_list:
#     if item == "musmatta":
#         break  # debug ,  break , continue
#     print('köp ' + item)
#
# print('Inköplista färdig!')


shoppin_list = ['dator', 'monitor', 'musmatta', 'mus', 'tangentbord']
item_to_find = 'kabel'
found_at = None
for index in range(len(shoppin_list)):
    if shoppin_list[index] == item_to_find:
        found_at = index
        break
if found_at:
    print('vårat sökta föremål på position {}'.format(found_at))
else:
    print('föremålet fanns inte i listan')
