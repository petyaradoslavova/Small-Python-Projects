import turtle
colors = ["purple","magenta","cyan","blue"]
my_pen = turtle.Pen()
my_pen.shape("turtle")
turtle.bgcolor("black")
for x in range(360):
    my_pen.pencolor(colors[x%4])
    my_pen.width(int(x/40 + 1))
    my_pen.forward(x)
    my_pen.left(24)

