def digital_root(n):
    def f(x): return sum([int(x) for x in str(n)])
    return digital_root(str(f(n))) if len(str(f(n))) != 1 else f(n)
print (digital_root(912))
