import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("Purple") #Background color

# Create a turtle

Abdi = turtle.Turtle()
Abdi.pensize(4)
Abdi.color("white")


# Draw a square 
for _ in range (4):
    Abdi.forward(100)
    Abdi.right(90)


#Finish
turtle.done()