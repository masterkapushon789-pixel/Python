for n in range(78):

    b = bin(n)[2:]


    b = b + str(b.count('1') % 2)
    b = b + str(b.count('1') % 2)


    r = int(b, 2)


    if r > 97:
        print(r)


        break

