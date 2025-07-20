import turtle #Importig libary
turtle.Screen().bgcolor("purple")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle() #definied variable

num_sides = 6 #variable
side_length = 70
angle = 360.0 / num_sides
#iterate loop for total number of side
for i in range (num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()