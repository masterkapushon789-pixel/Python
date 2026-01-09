# Решение
from itertools import permutations

table = '15 16 26 27 29 35 37 38 48 49 51 53 58 61 62 67 72 73 76 83 84 85 92 94'
graph = 'аб аг ае ба бв вб вд вк га гд ге дв дг дк еа ег еж же жи иж ик кв кд ки'

for p in permutations('абвгдежик'):
    newgraph = table
    for i in range(1, 10):
        newgraph = newgraph.replace(str(i), p[i - 1])
        if set(newgraph.split()) == set(graph.split()):
            print(p)






answer = 37

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 14, answer, 'a5bfc9e07964f8dddeb95fc584cd965d'))