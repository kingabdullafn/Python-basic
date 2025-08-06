import math

def run_it_for_the_circle (r):

    c = 2 * math.pi * r
    return c

# Allows user to enter radius
print("Yo fam, welcome ro the circle ting calculator")
radius = float(input("Drop the radius bruv (in cm or whatever"))

#run the ting
circumference = run_it_for_the_circle(radius)

#show the g the results
print(f"Safe G, the circumference is: {circumference:.2f}units!")