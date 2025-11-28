# Решение

k = 0
l = 0

from turtle import *
tracer(0)
koef = 20
x = 1

for x in range(1, 100):

    k += 1
    if k >= 4:
        l += 1

    a = 3 * x - 1 + x
    b = x * (x + l)

    print(x, l, a ** 2 - 2 * b)


forward((x + 2) * koef)

for i in range(4):
    forward(x * koef)
    right(90)
    forward((x + 2) * koef)

right(90)
forward((x + 2) * koef)

for i in range(4):
    right(90)
    forward((3 * x - 1) * koef)

up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()

answer = 13

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 61, answer, 'aab3238922bcc25a6f606eb525ffdc56'))