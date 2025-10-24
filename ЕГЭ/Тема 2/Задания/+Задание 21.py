# Решение
from itertools import product, permutations


def f1(w, x, y, z):
    return 1 if ((x <= y) or (z <= w)) and ((z == y) <= (w == x)) else 0


for a0, a1, a2, a3 in product((0, 1), repeat=4):
    t = [(a0, 1, 0, a1, 0),
         (0, 1, 0, 1, 0),
         (a2, 1, 0, a3, 0)]
    if len(set(t)) == len(t):
        for w, x, y, z in permutations((0, 1, 2, 3)):
            if all([f1(i[w], i[x], i[y], i[z]) == i[-1] for i in t]):
                print(f'w = {w + 1}; x = {x + 1}; y = {y + 1}; z = {z + 1}')
                break

answer = "yxwz"

#

from tests.conftest import result_register

if answer is not Ellipsis:
    print(result_register(2, 21, answer, '1ed5bb3720986c091b8dc2704366e53d'))
