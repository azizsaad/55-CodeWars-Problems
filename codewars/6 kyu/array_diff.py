def array_diff(a, b):

    # result = []
    # for i in a:
    #     if i in b:
    #         pass
    #     else:
    #         result.append(i)
    # return result

    return list(filter(lambda x : x not in b, a))

print (array_diff([1,1,2,2,3,3], [2,3]))
