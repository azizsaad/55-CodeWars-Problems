def printer_error(s):
    dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    count = len(s)
    count_out = 0
    for i in s:
        if i not in dict:
            count_out += 1
    return '{}/{}'.format(count_out,count)



    return

print (printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))
