from itertools import product

print('x y z w')
for x, y, z, w in product([0, 1], repeat=4):
    if not ((x and not (y)) or (x == z) or w):
        print(x, y, z, w)
