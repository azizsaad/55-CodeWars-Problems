def solution(number):
    return sum([i for i in range(number) if not (i % 3) or not (i % 5)])

print (solution(10))

'''
def solution(number):
    var1 = 0
    for i in range(0,number):
        if i % 3 == 0 or i % 5 == 0:
            var1 += i
    return var1
'''
