from itertools import product, permutations
"""
for x1 in 'ABCD':
    for x2 in 'ABCD':
        for x3 in 'ABCD':
            for x4 in 'ABCD':
                print(x1, x2, x3, x4)
"""
"""

for x in product('ABCD', repeat=4):
    print(''.join(x))
"""

for x in product('AB', 'CD', 'AB', 'CD'):
    print(x)

"""
for p in permutations('ABCD', 3):
    print(p)
"""
