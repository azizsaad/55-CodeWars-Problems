def maskify(cc):
    hashed = ['#' for i in range(len(cc)-4)]
    hashed.append(cc[-4:])
    return ''.join(hashed)

print (maskify("4556364607935616"))
