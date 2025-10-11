from itertools import product

print('x y w z')
for x,y,w,z in product([0,1],repeat=4):
    if not((x and y or (not x)) and w or z):
        print(x,y,w,z)