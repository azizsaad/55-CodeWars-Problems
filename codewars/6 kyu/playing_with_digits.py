def dig_pow(n, p):
    n2 = [int(x) for x in str(n)]
    n3 = []

    for i,x in enumerate(n2):
        n3.append(pow(x,p))
        p = p + 1
    val = mysum(n3) // n
    calc = mysum(n3) % n
    if not calc:
        return val
    else:
        return -1

'''
def dig_pow(n, p):
    mysum = sum([pow(x,y) for x,y in zip([int(x) for x in str(n)], range(p,p+len(str(n))))])
    return mysum//n if not mysum%n else -1
n = 695
p = 1

print(dig_pow(695,1))
'''
