from itertools import permutations

table = '13 14 16 25 27 31 34 41 43 47 52 56 57 61 65 72 74 75'
graph = 'АБ АД БА БД БВ ВБ ВГ ГВ ГЕ ГЖ ДА ДБ ДЕ ЕД ЕГ ЕЖ ЖГ ЖЕ'

for p in permutations('АБВГДЕЖ'):
    new_graph = table
    for i in range(1, 8):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)
