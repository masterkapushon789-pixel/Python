# Решение
from itertools import permutations

t = '13 14 16 25 27 31 34 41 43 47 52 56 57 61 65 72 74 75'
g = 'аб ад бв ба бд вб вг гв ге гж дб да де ег ед еж жг же'

for p in permutations('абвгдеж'):
    nigga = t
    for i in range(1, 8):
        nigga = nigga.replace(str(i), p[i - 1])
    if set(nigga.split()) == set(g.split()):
        print(p)






answer = 7

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 18, answer, '8f14e45fceea167a5a36dedd4bea2543'))