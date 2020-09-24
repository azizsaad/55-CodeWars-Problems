def square_digits(num):
    result = [int(x) for x in str(num)]
    return int(''.join(str(i) for i in [i**2 for i in result]))


print (square_digits(9119))
