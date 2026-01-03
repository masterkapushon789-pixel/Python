a = 0
from itertools import permutations
for line in permutations('ОЛЬГА', 5):
    line = ''.join(line)
    if line[0] != 'Ь' and line.count('ОЬ') == 0 and line.count('АЬ') == 0:
        a += 1
print(a)