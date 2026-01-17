for n in range(4, 78999999):


    b = bin(n)[2:]


    b = b.replace('0','x').replace('1', '0').replace('x', '1')


    b = b.lstrip('0')

    if len(b) == 0:
        continue


    b = int(b, 2)


    r = n - b


    if r == 999:
        print(n)


        break

