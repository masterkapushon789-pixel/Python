# Решение
import math
s = 1024 * 768
p = 4096
i = math.log2(p)
v = s * i
v = v - 0.2 * v
a = 200 * (2 ** 13)
print(v / a)







answer = 5

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(7, 16, answer, 'e4da3b7fbbce2345d7772b0674a318d5'))