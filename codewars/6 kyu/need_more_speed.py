
#METHOD 1

list = [1,2,3,4,5]
newlist = []

for i in range(len(list)-1,-1,-1):
    newlist.append(list[i])
print (newlist)


#METHOD 2

'''
def reverse(list):
    list.reverse()
    return list
print (reverse([1,2,3,4]))
'''
