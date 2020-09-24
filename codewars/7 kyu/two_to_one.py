def longest(s1, s2):
    var1 = sorted(set((s1)))
    var2 = sorted(set((s2)))
    for i in var2:
        var1.append(i)
    return ''.join(sorted(set((var1))))

print (longest("aretheyhere", "yestheyarehere"))
