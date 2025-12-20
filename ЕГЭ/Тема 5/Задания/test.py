b = 0
n2 = '100'
for i in range(0, len(n2), 2):
    if n2[i] == '0':
        b += 1
        print(b)