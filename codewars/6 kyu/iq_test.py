def iq_test(numbers):
    num = [int(i) for i in numbers.split(' ')]

    eo_count = 0

    for i in num:
        if i % 2 == 0:
            eo_count += 1

    for i,x in enumerate(num):
        if eo_count == 1:
            if x % 2 == 0:
                return (i+1)
        else:
            if x % 2 != 0:
                return (i+1)

'''
def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    print (e)

print (iq_test('1 2 3 4'))
'''
