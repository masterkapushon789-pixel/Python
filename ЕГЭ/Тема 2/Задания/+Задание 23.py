# Решение
from itertools import product

print('w x y z')

for w, x, y, z in product([0, 1], repeat=4):
    if ((not x) and (z) and (not y) and (not w)) or ((not x) and (z) and (y) and (not w)) or ((not x) and (z) and (y) and (w)):
        print(w, x, y, z)






answer = 'xywz'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 23, answer, '00e936354216c4a6823136059258f377'))