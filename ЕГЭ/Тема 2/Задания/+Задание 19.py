# Решение
from itertools import product

print('u w x y z')
for u, w, x, y, z in product([0, 1], repeat=5):
    f = ((x <= y) and (z == (not w))) <= (u == (x or z))
    if not f:
        print(u, w, x, y, z)

answer = 'wzyxu'

#

from tests.conftest import result_register

if answer is not Ellipsis:
    print(result_register(2, 19, answer, 'b83215ff76ddd410e32571919b78d0eb'))
