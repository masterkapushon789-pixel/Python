from math import *
# Решение
n = 102
v = 53 * 1024 * 1024
i = v // 282_952 * 8 // n
a = 2 ** i
print(a)





answer = 32768

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(11, 113, answer, 'f43764367fa4b73ba947fae71b0223a4'))