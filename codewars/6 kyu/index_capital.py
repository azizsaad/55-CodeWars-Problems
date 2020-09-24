def capital(s,ind):

    s2 = list(s)

    for i in ind:

        s2[i] = s2[i].upper()

    print (''.join(s2))

capital('saadaziz',[0,4,7])
