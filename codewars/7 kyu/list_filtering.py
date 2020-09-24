def filter_list(l):
    result = []
    for i in l:
        if type(i) != str:
            result.append(i)
    return result

print (filter_list([1,2,'a','b']))
