# Решение
from itertools import permutations

table =   '12 14 16 18 21 23 25 27 32 35 37 41 48 52 53 56 57 61 65 68 72 73 75 81 84 86'
ktotytg = 'аб ад ба бв бе вб вг ве вж ви гв ги да дб де еб ев ед еж жв же жи ив иг иж   '

for p in permutations('абвгдежи'):
    yvnkxx = table
    for i in range(1, 9):
        yvnkxx = yvnkxx.replace(str(i), p[i - 1])
    if set(yvnkxx.split()) == set(ktotytg.split()):
        print(p)





answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 17, answer, '37693cfc748049e45d87b8c7d8b9aacd'))