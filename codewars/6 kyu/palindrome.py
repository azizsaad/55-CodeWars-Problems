'''
s = 'qqnbnb'

rev = ''.join(reversed(s))

for i in range(len(rev),0,-1):
    if rev[:i] in s:
        key = rev[:i]
        # print(key)
        cutoff = s.index(key[0])
        # print (cutoff)
        add_on = s[:cutoff]
        # print (add_on)
        answer = s+add_on
print (answer)
'''

def build_palindrome(s):
    a = s[1:][::-1] + s

    print (a+'\n')

    temp = s
    for i in range(len(s)+1):
        temp = s[::-1][:i] + s
        if temp == temp[::-1] and len(temp)<len(a):
            a = temp

    b = s + s[::-1]
    temp = s
    for i in range(len(s)+1):
        temp = s + s[::-1][i:]
        if temp == temp[::-1] and len(temp)<len(b):
            b = temp
    if len(a)>len(b):
        return b
    else:
        return a

print (build_palindrome('nbnb'))


mystr = "what is going on here"
print(mystr[:0][::-1])
