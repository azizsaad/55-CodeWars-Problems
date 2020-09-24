word = ("Reeady @)")

result = []

for i in word.lower():

    if word.lower().count(i) == 1:
        result.append('(')
    else:
        result.append(')')

print(''.join(result))
