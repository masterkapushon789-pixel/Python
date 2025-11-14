# Решение
a = []
for n in range(1, 50):
    n2 = bin(n)[2:]
    n2 += bin(n % 4)[2:]
    r = int(n2, 2)
    a.append(r)
print(len(a))






answer = 49

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 14, answer, '1f0e3dad99908345f7439f8ffabdffc4'))