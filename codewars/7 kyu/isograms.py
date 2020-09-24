def is_isogram(string):
    if string == '':
        return True
    string2 = [str(x) for x in string.lower()]
    count = []
    for i,x in enumerate(string2):
        count.append(string2.count(x))
    if max(count) > 1:
        return False
    else:
        return True

print (is_isogram("moOse"))
