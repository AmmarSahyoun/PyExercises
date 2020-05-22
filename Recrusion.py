# def cleanWord(word):
#     if len(word) == 1 :
#         return word
#     if word[0] == word[1]:
#         #print(f'PRINTING before condition {word}')
#         return cleanWord(word[1:])
#     #print(f'PRINTING before return {word}')
#     return word[0] + cleanWord(word[1:])
#
# print(cleanWord("wwwwooorlddd"))

print('+++++++++++++Lambda++++inline++++++oneSingleFunction++++')

def sayHello(name) : return f"Hello {name}"
var = lambda name: f"hello {name}"

print(sayHello.__name__) # wha is the name of this function
print(var.__name__) # wha is the name of this function

play = lambda sport: "let's play "+ sport
playm = lambda music: 'lets play' + music
print(play('basketball'))
print(playm('guitar'))