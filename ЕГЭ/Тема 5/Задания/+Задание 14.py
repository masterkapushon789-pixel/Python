# Решение
a = [0] * 10000
for n in range(1, 1000):
    n2 = bin(n)[2:]
    n2 += bin(n % 4)[2:]
    r = int(n2, 2)
    a[r] = 1

m = 0
for i in range(0, 10000 - 49):
    count = a[i:i+49].count(1)
    if count > m:
        m = count
print(m)

#  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ...
# [0 0 0 1 0 1 1 1 0 1 1  1  0  1  1  1  1  0  1  1 ]






answer = 19

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 14, answer, '1f0e3dad99908345f7439f8ffabdffc4'))