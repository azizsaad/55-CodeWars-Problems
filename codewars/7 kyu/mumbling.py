def accum(s):
    var1 = list(s)
    result = []
    count = 1
    for i,x in enumerate(var1):
        result.append(x.lower()*count)
        count += 1

    result2 = [item.capitalize() for item in result]
    return '-'.join(result2)

print (accum("ZpglnRxqenU"))
