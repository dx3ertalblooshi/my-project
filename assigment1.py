import turtle

GLOBAL_ANGLE=45

def testing():
    t=turtle
    t.pendown()
    t.fd(100)
    t.goto(50,100)
    t.circle(50)

def turtle_state():
    pen=turtle.isdown()
    heading=turtle.heading()
    x=turtle.xcor()
    y=turtle.ycor()
    print("t is down:",pen,"turtle direction angle:",heading, "x coordinate", x ,"y coordinate", y) 


def square(size, angle, line_color, fill_color):
    turtle.pencolor(line_color)  # pen color and changes as it goes
    turtle.fillcolor(fill_color)   # filling the square with color
    turtle.begin_fill()  # begin filling
    turtle.setheading(angle)
    turtle.pendown()
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.end_fill()  # end fill
    turtle.hideturtle()

def main():
    square(20, GLOBAL_ANGLE, "red", "blue")
    square(40, GLOBAL_ANGLE, "red", "black")
    square(60, GLOBAL_ANGLE, "black", "green")
    
main()

