a1 = ['my','name','is','saad','jackson','solomanitisitis']
a2 = ['incredibly','reject','expeditiously']

a1max = len(max(a1,key=len))
a1min = len(min(a1,key=len))

a2max = len(max(a2,key=len))
a2min = len(min(a2,key=len))


if a1max > a2max:
    diff = a1max - a2min
elif a2max > a1max:
    diff = a2max - a1min


print (diff)
