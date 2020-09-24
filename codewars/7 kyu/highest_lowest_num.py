def high_and_low(numbers):
    num = [int(x) for x in numbers.split(' ')]
    result = [max(num),min(num)]
    return ' '.join(str(x) for x in result)



print (high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
