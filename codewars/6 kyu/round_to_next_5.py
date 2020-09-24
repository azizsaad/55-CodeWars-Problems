'''
num = input('enter a number:')
num2 = int(num)
print (num2)


var1 = num2 / 5
print (var1)

rem = int(var1)
print (rem)

rem2 = rem * 5
print (rem2)

if num2-rem2 >= 2.5:
    result = rem2 + 5
else:
    result = rem2

print (result)

'''


def round_to_next5(n):
    return n + (5 - n) % 5

print (round_to_next5(14))
