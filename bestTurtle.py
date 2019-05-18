import turtle

tortoise = turtle.Turtle()

def bepis(length):
    for i in range(0, 5):
        tortoise.forward(length)
        tortoise.right(144)

    length = length * 3.14
    arc = length / 360
    tortoise.right(108)
    for i in range(0, 361):
        tortoise.forward(arc)
        tortoise.left(1)

def spiral(angle, dist, step):
    g = dist
    while g >= 0:
        tortoise.forward(g)
        tortoise.right(angle)
        g = g - step

def loopyDoo(sides, corner, distance, turn = 1, shift = 1):
    corner =  corner - 180
    for i in range(0, (360 // turn):
        for j in range(0, sides):
            tortoise.right(corner)
            tortoise.forward(distance)
        tortoise.right(turn)
        tortoise.forward()
