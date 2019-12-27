import turtle

turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.speed('fastest')
turtle.bgcolor('black')

def levy_line (l ,n):
    if n == 0:
        turtle.forward(l)
    else:
        turtle.color('red')
        turtle.left(45)
        levy_line(l, n-1)
        turtle.color('orange')
        turtle.right(90)
        levy_line(l, n-1)
        turtle.left(45)        

levy_line(15,15)

turtle.exitonclick()
