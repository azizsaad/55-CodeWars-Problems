def disemvowel(string):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    result = []
    for i in string:
        if i not in vowels:
            result.append(i)
    return ''.join(str(x) for x in result)

print (disemvowel("This website is for losers LOL!"))
