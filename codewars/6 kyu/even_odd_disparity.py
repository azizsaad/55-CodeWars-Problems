def solve(a):

    e_count = 0
    o_count = 0

    newlist = [i for i in a if isinstance(i,int)]


    for i in newlist:

        if i%2==0:
            e_count += 1
        elif i%2 != 0:
            o_count += 1

    print(e_count - o_count)

solve ([1,8,8,8,8,'a'])
