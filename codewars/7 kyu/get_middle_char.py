def get_middle(s):

    if s == []:
        return ''
    var1 = list(s)
    print (var1)

    if len(var1) == 1 or len(var1) == 2:
        return ''.join(var1)
    else:
        for i in range(len(var1)+1):
            var1.pop(-1)
            var1.pop(0)
            print (var1)
            if len(var1) == 1 or len(var1) == 2:
                return ''.join(var1)

print (get_middle("qdXHXeSVWQmgN"))
