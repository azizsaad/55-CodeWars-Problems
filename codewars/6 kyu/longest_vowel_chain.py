
word = input('Enter a word: ')
vowels = ['a','e','i','o','u']

substring = 0
count = []

for i,x in enumerate(word):

    if x in vowels:
        substring += 1
    else:
        substring = 0

    count.append([substring])

print (max(count)[0])
