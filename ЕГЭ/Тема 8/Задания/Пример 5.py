c = 1
from itertools import *
for a in product('акорст', repeat=5):
    if a[0] not in 'аст' and a.count('о') == 2 and c%2==0:
        print(c)
    c += 1