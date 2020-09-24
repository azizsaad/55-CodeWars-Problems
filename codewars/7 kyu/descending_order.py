def descending_order(num):
    result = [int(x) for x in str(num)]
    var1 = sorted(result)
    return int(''.join(str(i) for i in (var1[::-1])))

print (descending_order(74869))
