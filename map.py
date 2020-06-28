names = ['AMMaR  ', 'LuBNa  ', 'PAul']


def format(text):
    return f" - {text.strip().capitalize()} -"


result = map(format, names)  # map(function, data)
for i in result:
    print(i)
print('++++++++++++++++++++++')
for p in list(map(lambda d: f" - {d.strip()} -", names)):
    print(p)
print('--------------------')
calc = lambda x, y: x if x > y else y
print(calc(2, 4))

print('--------------------')
fa= lambda a,b: a if a+b>a else f"Maniak elDeres"
print(fa(2,-3))
