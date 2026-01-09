# Решение
from itertools import permutations

table = '16 17 23 25 26 32 34 37 43 45 52 54 56 61 62 65 71 73'
graph = 'ac ae bg bd cg cf ca db de ed ef ea fc fe fg gb gf gc'

for p in permutations('abcdefg'):
    new_graph = table
    for i in range(1, 8):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)

answer = 14

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 13, answer, 'aab3238922bcc25a6f606eb525ffdc56'))