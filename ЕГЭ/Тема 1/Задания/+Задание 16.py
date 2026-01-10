# Решение
from itertools import permutations

table =     '15 18 23 25 32 35 36 45 47 51 52 53 54 56 57 58 63 65 74 75 78 81 85 87'
artemgraf = 'ab ac ad ae af ag ah bc ba cd cb ca dc da ef ea fe fg fa gf gh ga hg ha'
print('  1    2    3    4    5    6    7    8')
for p in permutations('abcdefgh'):
    newartemgraf = table
    for i in range(1, 9):
        newartemgraf = newartemgraf.replace(str(i), p[i - 1])
    if set(newartemgraf.split()) == set(artemgraf.split()):
        print(p)






answer = 48

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 16, answer, '642e92efb79421734881b53e1e1b18b6'))