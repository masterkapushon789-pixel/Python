# Решение
from itertools import product

print('w x y z')
for w, x, y, z in product([0, 1], repeat=4):
    if ((x == y) <= ((not z) or w)) == (not ((w <= x) or (y <= z))):
        print(w, x, y, z)
answer = 'wzyx'

#

from tests.conftest import result_register

if answer is not Ellipsis:
    print(result_register(2, 2, answer, 'e0abee87e4ba1de22c6b8cf076c5016b'))
