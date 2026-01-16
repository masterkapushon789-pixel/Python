# Решение
from itertools import product

print('w x y z')
for w, x, y, z in product([0, 1], repeat=4):
    if (x == (y <= z)) and (y == (not (z <= w))):
        print(w, x, y, z)
    if not(x == (y <= z)) and (y == (not (z <= w))):
        print(w, x, y, z)





answer = 'wyxz'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 24, answer, 'c5e4e768af58cf865c4006af69319e62'))