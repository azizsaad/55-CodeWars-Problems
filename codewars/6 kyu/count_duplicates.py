text = ("aabbcdee")

letters = {}

for i in text:
    text2 = i.lower()
    if text2 in letters.keys():
        letters[text2] += 1
    else:
        letters[text2] = 1
print (letters)

count = 0
for i in letters:
    if letters[i] > 1:
        count += 1
print (count)




'''
>>> inputstring = 'A=Astring,B=Bstring,C=Cstring'
>>> dict(entry.split('=') for entry in inputstring.split(','))
{'A': 'Astring', 'C': 'Cstring', 'B': 'Bstring'}
'''
