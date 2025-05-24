import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.penup()
t.speed(1)
t.shape("turtle")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta", "lime", "#CCCCFF"]

for i in range(10):
    t.color(colors[i % len(colors)])
    t.forward(100)
    t.stamp()
    t.backward(100)
    t.right(36)

for i in range(10):
    t.color(colors[-(i+1)])
    t.forward(60)
    t.stamp()
    t.backward(60)
    t.right(36)

turtle.exitonclick()
