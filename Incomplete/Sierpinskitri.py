import turtle

t = turtle.Turtle()
t.shape("turtle")

t.penup()
t.setpos(-375,-325) # relative pixel positions
t.pendown()

k = 2

def koch(t, order = k, size = 750):
    if k == 0:
        t.forward(size)
        t.left(120)
        t.forward(size)
        t.left(120)
        t.forward(size)
    else:
        t.forward(size)
        t.left(120)
        t.forward(size)
        t.left(120)
        t.forward(size)
        t.left(120)
        koch(t, k - 1, size/2)

koch(t, k)

wn = turtle.Screen()

wn.exitonclick()
turtle.bye()