import turtle

turtle.shape('turtle')
turtle.speed(100)
for i in range(1000):
    turtle.forward(0.2 + 0.1 * i)
    turtle.left(10)