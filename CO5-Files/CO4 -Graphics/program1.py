import turtle

t = turtle.Turtle()
t.speed(1000)
t.pensize(20)
turtle.bgcolor("black")

colors = ["red", "yellow"]
for i in range(400):
    t.color(colors[i % 2]) 
    t.circle(100)
    t.right(10)

turtle.done()
