text = "The sunset sets at twelve o' clock."
text1 = text.lower()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = []

for letter in text1:
    if letter in alphabet:
        result.append(alphabet.index(letter)+1)

s = [str(i) for i in result]
result2 = ' '.join(s)
print (result2)
