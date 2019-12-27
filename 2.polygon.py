import turtle
import math
turtle.shape('turtle')
turtle.bgcolor('black')
turtle.color('orange')

n=5
r=15 
def more_agles(n,l):
    q=360/n
    while n>0:
        
        turtle.left(q)
        turtle.forward(l)
        n-=1
while n<13:
    l=2*r*math.sin(math.pi/n)
    x=(180-360/n)/2
    turtle.left(x)
    
    more_agles(n,l)
    turtle.right(x)
    turtle.penup()
    turtle.forward(5)
    
    turtle.pendown()
    n+=1
    r+=5
