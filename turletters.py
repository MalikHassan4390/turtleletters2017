import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        tur.setpos(40, 0)
        tur.pendown()
    elif letter == "B":
	    pass
    elif letter == "C":
	tur.penup()
        tur.right(90)
        tur.forward(5)
        tur.right(90)
        tur.forward(10)
        tur.pendown()
        tur.right(-90)
        tur.forward(30)
        tur.right(180)
        tur.forward(30)
        tur.right(-90)
        tur.forward(40)
        tur.right(-90)
        tur.forward(30)
        tur.penup()
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(40)
        tur.right(180)
        tur.fd(40)
        tur.right(90)
        tur.fd(30)
        tur.left(180)
        tur.fd(30)
        tur.left(90)
        tur.fd(18)
        tur.left(90)
        tur.fd(25)
        tur.pu()
        tur.setpos(40, 0)
    elif letter == "G":
	    pass		
    elif letter == "H":

        tur.setheading(0)
        tur.penup()
        tur.forward(5)
        tur.right(90)
        tur.forward(5)
        tur.pendown()
        tur.forward(50)
        tur.penup()
        tur.backward(25)
        tur.left(90)
        tur.pendown()
        tur.forward(30)
        tur.left(90)
        tur.backward(25)
        tur.forward(50)
        tur.penup()
        tur.forward(5)
        tur.right(90)
        tur.forward(5)
        tur.pendown()

    elif letter == "I":
	    tur.pu()
        tur.right(180)
        tur.fd(5)
        tur.left(90)
        tur.forward(5)
        tur.pd()
        tur.forward(30)
        tur.right(180)
        tur.forward(15)
        tur.left(90)
        tur.fd(50)
        tur.right(90)
        tur.forward(15)
        tur.right(180)
        tur.forward(30)
        tur.pu()
        tur.forward(5)
        tur.left(90)
        tur.forward(55)
        tur.right(90)
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	    pass
    elif letter == "M":
	tur.penup()
        tur.forward(5)
        tur.right(90)
        tur.forward(40)
        tur.left(90)
        tur.forward(5)
        tur.pendown()
        tur.right(65)
        tur.forward(40)
        tur.right(180)
        tur.forward(40)
        tur.left(140)
        tur.forward(30)
        tur.right(140)
        tur.forward(30)
        tur.left(140)
        tur.forward(40)
    elif letter == "N":
	    pass
    elif letter == "O":
	tur.setheading(0)
        tur.penup()
        tur.forward(20)
        tur.right(90)
        tur.forward(48)
        tur.left(90)
        tur.pendown()
        tur.circle(18)
        tur.penup()
        tur.left(90)
        tur.forward(48)
        tur.right(90)
        tur.forward(20)
    elif letter == "P":
	    pass		
    elif letter == "Q":
	tur.setheading(0)
        tur.penup()
        tur.forward(5)
        tur.right(90)
        tur.forward(30)
        tur.pendown()
        tur.circle(15,360)
        tur.penup()
        tur.setheading(0)
        tur.forward(15)
        tur.pendown()
        tur.setheading(315)
        tur.forward(22)
        tur.penup()
        tur.setheading(0)
        tur.forward(4)
        tur.left(90)
        tur.forward(46)
        tur.setheading(0)
    elif letter == "R":
	    pass
    elif letter == "S":
        tur.setheading(0) 
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(90)
        tur.fd(30)
        tur.left(180)
        tur.fd(30)
        tur.left(90)
        tur.fd(25)
        tur.left(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(25)
        tur.right(90)
        tur.fd(30)
        tur.pu()
        tur.setpos(40, 0)
        tur.right(180)
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
        tur.setheading(0)
        tur.penup()
        tur.forward(20)
        tur.right(90)
        tur.forward(60)
        tur.right(180)
        tur.pendown()
        tur.left(20)
        tur.forward(45)
        tur.backward(45)
        tur.right(40)
        tur.forward(45)
        tur.backward(45)
        tur.left(20)
        tur.penup()
        tur.forward(60)
        tur.right(90)
        tur.forward(20)
        tur.pendown()
    elif letter == "W":
	    pass
    elif letter == "X":
        tur.setheading(0)
        tur.pu()
        tur.right(45)
        tur.pd()
        tur.fd(55)
        tur.pu()
        tur.fd(-55)
        tur.right(-45)
        tur.fd(40)
        tur.right(135)
        tur.pd()
        tur.fd(55)
        tur.pu()
        tur.fd(-55)
        tur.right(-135)

    elif letter == "Y":
	tur.setheading(0)
        tur.penup()
        tur.forward(4)
        tur.right(90)
        tur.forward(10)
        tur.left(45)
        tur.pendown()
        tur.forward(23)
        tur.left(90)
        tur.forward(23)
        tur.right(180)
        tur.forward(23)
        tur.right(315)
        tur.forward(23)
        tur.penup()
        tur.right(180)
        tur.forward(50)
        tur.right(90)
        tur.forward(20)
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)

window = turtle.Screen()
tur = turtle.Turtle()


tur.speed(1)
turtleLetter("box",tur)
turtleLetter("F",tur)




window.exitonclick()

