from itertools import product
index = 1
for line in product('АПРСУ', repeat=5):
    line = ''.join(line)
    if line.count('AA') == 0 and line.count('У') <= 1:
        print(index)
    index += 1