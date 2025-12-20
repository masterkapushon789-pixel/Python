# Решение
for n in range(0, 9999):
    n2 = bin(n)[2:]
    n2 = n2.replace('0', '2')
    n2 = n2.replace('1', '0')
    n2 = n2.replace('2', '1')
    n2 = int(n2, 2)
    r = n - n2
    if r == 999:
        print(n)
        break






answer = 1011

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 5, answer, '7f975a56c761db6506eca0b37ce6ec87'))