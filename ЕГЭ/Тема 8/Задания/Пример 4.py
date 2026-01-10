c = 0
from itertools import *
for a in permutations('митрофан', 6):
    a = ''.join(a)
    if 'ио' not in a and 'ои' not in a and 'иа' not in a and 'аи' not in a and 'оа' not in a and 'ао' not in a:
        if (a.count('м') + a.count('т') + a.count('р') + a.count('ф') + a.count('н')) > (a.count('и') + a.count('о') + a.count('а')):
            c += 1
print(c)