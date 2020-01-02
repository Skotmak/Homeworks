from turtle import *
instruction = ['l', 'f', 'r', 'f', 'l']


def movement(iterations=1, actions=None, length=None):
    if not actions:
        actions = ['f']
    if not length:
        length = 200 / 2 ** (iterations/2)
    for i in actions:
        if i == 'f':
            if iterations != 0:
                movement(iterations - 1, instruction, length)
            else:
                forward(length)
        elif i == 'l':
            left(45)
        elif i == 'r':
            right(90)

iterations = 18
speed(0), tracer(0, 0)
movement(iterations)
update()
mainloop()