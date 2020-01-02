import turtle 

def square(color,leight,x,y):
    i=0
    turtle.shape("turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    while i<4:
        turtle.left(90)
        turtle.forward(leight)
        i += 1 

square("black",50,0,0)
square("red",70,10,-10)
square("blue",90,20,-20)
square("yellow",110,30,-30)
square("green",130,40,-40)
square("black",150,50,-50)
square("red",170,60,-60)
square("blue",190,70,-70)
square("yellow",210,80,-80)
square("green",230,90,-90)
turtle.exitonclick()