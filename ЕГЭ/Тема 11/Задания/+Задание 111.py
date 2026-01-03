# Решение

from math import *

'''
n - длина сообщения
v - сколько занимает памяти
i - объём одного символа
a - мощность алфавита
'''

n1 = 1
a1 = 6

n2 = 11
a2 = 20

n3 = 1
a3 = 1999

v = ceil(1188/36) # байт

i1 = ceil(log2(a1))
i2 = ceil(log2(a2))
i3 = ceil(log2(a3))

v1 = n1 * i1 # бит
v2 = n2 * i2 # бит
v3 = n3 * i3 # бит

vnad = ceil((v1 + v2 + v3) / 8)

ad = v - vnad

print(ad)

answer = 24

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(11, 111, answer, '1ff1de774005f8da13f42943881c655f'))
