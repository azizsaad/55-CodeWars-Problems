lines = ['a','b','c','d']
a = []

for i,x in enumerate(lines,1):
    var = str(i) + ': ' + str(x)
    a.append(var)

print (a)
