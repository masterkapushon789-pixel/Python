# Решение
from turtle import *
tracer(0)
koef = 20

for i in range(2):
    forward(3 * koef)
    left(90)
    backward(10 * koef)
    left(90)

up()

backward(10 * koef)
right(90)
forward(8 * koef)
left(90)

down()

for i in range(2):
    forward(16 * koef)
    right(90)
    forward(8 * koef)
    right(90)

up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()


answer = 12

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 6, answer, 'eecca5b6365d9607ee5a9d336962c534'))