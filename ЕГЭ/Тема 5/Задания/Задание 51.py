# decision
for n in range(1, 100):

    # 1
    n2 = bin(n)[2:]

    # 2
    a = n % 3
    a = bin(a)[2:]
    n2 += a

    # 3
    n10 = int(n2, 2)
    a = n10 % 5
    a = bin(a)[2:]
    n2 += a

    #4
    r = int(n2, 2)
    print(n, r, r//n)

answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 51, answer, '389499b02f30212486e408cd73a5bc50'))