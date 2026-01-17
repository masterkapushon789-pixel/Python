from turtle import *
tracer(0)
koef = 20
x = 5
for i in range(4):
    forward(x * koef)
    right(90)
    forward(x * koef)
    left(90)
    forward(x * koef)
    right(90)

up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()

for x in range(1, 1000):
    if ((x-1)*(x-2)*4)+((x-1)**2) > 1000:
        print(x)
        break
