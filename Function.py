def python_food():
    width = 80
    text = 'Spagetti med Köttfärssås'
    larf_margin = (width - len(text)) // 2
    print(' ' * larf_margin, text)


def center_text(text):
    width = 80
    left_margin = (width - len(text)) // 2
    centered_text = (' ' * left_margin) + text
    return centered_text

# python_food()

string1 = center_text('Detta ska centras')
print(string1)