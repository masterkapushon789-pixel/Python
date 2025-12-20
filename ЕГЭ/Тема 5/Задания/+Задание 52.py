# Решение
for n in range(2, 10000):
    a = 0
    b = 0
    n2 = bin(n)[2:]
    for i in range(1, len(n2), 2):
        if n2[i] == '1':
            a += 1
    for i in range(0, len(n2), 2):
        if n2[i] == '0':
            b += 1
    r = abs(a - b)
    if r == 5:
        print(n, r, n2, a, b)

answer = 1023

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 52, answer, 'ce5140df15d046a66883807d18d0264b'))