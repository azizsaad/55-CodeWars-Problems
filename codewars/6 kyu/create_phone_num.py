def create_phone_number(n):

    return '('+ ''.join(str(x) for x in n[0:3]) + ')' + ' ' + ''.join(str(x) for x in n[3:6]) + '-' + ''.join(str(x) for x in n[6:])

print (create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


# (123) 456-7890"

# n = [0,1,2,3]
# n2 = ','.join(str(x) for x in n)
# print(type(n2))

print (sum(1,2))
