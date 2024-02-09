from turtle import*


#we want to paint a house

#step 1: draw a square
speed(1111111)
width(7)

forward (200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drowing a door
begin_fill()

forward(70)
left(90)

forward(100)
right(90)

forward(60)
right(90)
      
forward(100)
end_fill()
penup()
goto (200,200)

pendown()

begin_fill()
right(150)
forward (200)

left(120)
forward(200)
end_fill()

#drow a window

left(30)
forward(45)

left(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)


#drow a window

    

left(90)

forward(120)
left(90)

forward(200)
left(90)

forward(120)
left(90)

forward(40)
right(90)

forward(40)
right(90)

forward(40)


exitonclick()