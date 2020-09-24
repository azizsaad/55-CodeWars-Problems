integers = [1,2,3,5,7,9,11,13,15]

count = 0

for i in integers:
    if i % 2 == 0:
        count += 1

for i in integers:
    if count == 1 and i % 2 == 0:
        print (i)
    elif count != 1:
        for i in integers:
            if i % 2 != 0:
                print (i)

'''
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
'''
