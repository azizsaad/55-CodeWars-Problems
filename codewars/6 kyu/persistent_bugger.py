
from operator import mul
def persistence(n):
    return 0 if n<10 else persistence(reduce(mul,[int(i) for i in str(n)],1))+1

# n = 12
#
# def f(x): return [int(i) for i in str(x)]
# list = f(n)
# count = 0
# while len(list) != 1:
#     result = 1
#     count += 1
#     for i in list:
#         result = result * i
#     list = f(result)
