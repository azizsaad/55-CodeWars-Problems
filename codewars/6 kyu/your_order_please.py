def order(sentence):
    if sentence == '':
        return ''
    var2 = sentence.split(' ')
    print (var2)
    dict = [str(i) for i in range(1,10)]
    result = [i for i in range(len(var2))]
    for i,x in enumerate(var2):
        for letnum in x:
            if letnum in dict:
                result[int(letnum)-1] = x
    return ' '.join(result)

print (order("is2 Thi1s T4est 3a"))
