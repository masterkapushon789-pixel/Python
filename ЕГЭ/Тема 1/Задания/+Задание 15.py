# Решение
from itertools import permutations

table = '15 16 24 25 26 28 37 38 42 45 47 48 51 52 54 56 61 62 65 73 74 78 82 83 84 87'
graph = 'аб аг ае ба бг бд бж вд ви га гб ге гж дб дв дж ди еа ег жб жг жд жи ив ид иж'

for p in permutations('абвгдежи'):
    new_graph = table
    for i in range(1, 9):
        new_graph = new_graph.replace(str(i), p[i-1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)






answer = 19

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 15, answer, '1f0e3dad99908345f7439f8ffabdffc4'))