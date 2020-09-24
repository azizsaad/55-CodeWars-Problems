def find_short(s):
    var1 = s.split(' ')
    print (var1)
    lengths = []
    for i in var1:
        lengths.append(len(i))
    print (lengths)

    return min(lengths)

print (find_short("bitcoin take over the world maybe who knows perhaps"))
