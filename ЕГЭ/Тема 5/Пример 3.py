for n in range(10, 100):
    i = n
    for z in range(3):
        n2 = bin(n)[2:]
        n = str(n)
        count1 = sum(n.count(str(i)) for i in [1, 3, 5, 7, 9])
        count2 = sum(n.count(str(i)) for i in [2, 4, 6, 8, 0])
        if count2 > count1:
            n2 += '1'
        if count1 > count2:
            n2 += '0'
        if count1 == count2:
            n = int(n)
            if n % 2 == 0:
                n2 += '0'
            if n % 2 != 0:
                n2 += '1'
        n = int(n2, 2)
    print(i, n, n // i)

'''
123455 // 8 = 15431             123458
987654321 // 8 = 123456790      987654312
'''
"""count = 0
for i in range(123458, 987654312 + 1, 8):
    count+=1
print(count)"""