# Решение
from itertools import permutations

table = '12 15 18 21 27 35 36 46 48 51 53 58 63 64 67 72 76 81 84 85'
graph = 'ac ad ag bc bh ca cb cg da dh ef eg fe fh ga gc ge hb hd hf'

for p in permutations('abcdefgh'):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)






answer = 52

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 19, answer, '9a1158154dfa42caddbd0694a4e9bdc8'))