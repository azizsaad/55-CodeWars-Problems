'''
def nb_dig(n, d):

    var1 = list(range(0,n))

    list1=[]

    for i in var1:
        list1.append(i**2)
'''



n = int(input('Enter number: '))


k = int(input('Enter number for k: '))
var1 = list(range(0,n+1))
list1 = []
count = 0

for i in var1:
    list1.append(i**2)

for i in list1:
    j = str(i)
    item = str.split(j)
    #print (item)
    item2 = [int(item) for item in str(i)]
    print (item2)
    if k in item2:
        count += 1

print (count)
