from itertools import permutations

table = '15 16 24 25 26 28 37 38 42 45 47 48 51 52 54 56 61 62 65'
graph = 'АБ АД БА БД БВ ВБ ВГ ГВ ГЕ ГЖ ДА ДБ ДЕ ЕД ЕГ ЕЖ ЖГ ЖЕ'

for p in permutations('АБВГДЕЖ'):
    new_graph = table
    for i in range(1, 8):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)
