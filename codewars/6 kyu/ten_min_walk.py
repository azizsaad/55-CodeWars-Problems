
def is_valid_walk(walk):
    direct = {'n':1,'s':-1,'e':2,'w':-2}

    count = 0

    if len(walk) != 10:
        return False
    else:
        for i, num in direct.items():
            for j in walk:
                if j == i:
                    count += num
    if count == 0:
        return True
    else:
        return False

print (is_valid_walk(['n', 'e', 'n', 'w', 'n', 'n', 'w', 'w', 'n', 's']))
