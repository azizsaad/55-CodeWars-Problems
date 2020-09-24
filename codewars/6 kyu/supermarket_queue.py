def queue_time(customers, n):

    if customers == []:
        return 0

    tills = []
    for index, item in enumerate(customers):

        if len(tills) == n:
            val = tills.index(min(tills))
            tills[val] = tills[val] + item

        else:
            tills.append(item)

    return max(tills)

print (queue_time([2,2,3,3,4,4], 2))
