from turtle import Turtle, Screen
import random                     # so i can generate random colors later

turtle = Turtle()          # new turtle object to variable
turtle.shape("turtle")     # will become a turtle shape in the window
turtle.color("red")        # change colour of turtle       ( can also use other format to change color)

# Draw a square (use for loop to iterate through same actions)
#for movement in range(4):
#    turtle.forward(100)        # value is the distance
#    turtle.right(90)           # Value is an angle


# Draw a dashed line (uuse for loop to iterate)
#for movement in range(4):
#    turtle.pendown()             # will draw when moving
#    turtle.forward(30)
#    turtle.penup()               # no drawing when moving
#    turtle.forward(30)


# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
#no_of_sides = 3  # Since starts with triangle which has 3 sides
#for no_of_shapes in range(8):                 # iterate 8 times from 0 to 7 since there are 8 shapes to be created
#    direction_changed = 360 / no_of_sides
#    for movement in range(no_of_sides):       # will move based on number of sides of the shape
#        turtle.right(direction_changed)
#        turtle.forward(100)
#    no_of_sides += 1                          # since no_of_sides is greater by 1 from each shape


# Draw a Random Walk
#colour = ["Blue","Black","Lime","Yellow","Firebrick","RosyBrown","DeepPink","Purple","MediumSlateBlue"]    # Create list of colours
#directions = [0,90,180,270]      # Create list of directions turtle can face
#turtle.pensize(20)               # Set specific width of pensize
#turtle.speed('fast')             # Set speed of the rate where turtle will draw  (can use integer to represent too)
#for movement in range(150):
#    random_color = random.choice(colour)
#    random_direction = random.choice(directions)
#    turtle.color(random_color)             # choose a random color
#    turtle.forward(30)
#    turtle.setheading(random_direction)         # set orientation of turtle to certain angle


# ways to generate color other than creating a specific list of strings of color names
#import turtle as t
#t.colormode(255)        # set r,g,b values to be in range of 0-255

#def random_colour():
#    r = random.randint(0, 255)        # will get random value from 0 to 255
#    g = random.randint(0, 255)
#    b = random.randint(0, 255)
#    return (r, g, b)              # parentheses needed as need to pass in as a tuple to .color()

#directions = [0,90,180,270]      # Create list of directions turtle can face
#turtle.pensize(20)               # Set specific width of pensize
#turtle.speed('fast')             # Set speed of the rate where turtle will draw  (can use integer to represent too)
#for movement in range(150):
#    random_direction = random.choice(directions)
#    turtle.color(random_colour())             # choose a random color, by choosing random r,g,b values
#    turtle.forward(30)
#    turtle.setheading(random_direction)


# Draw a Spirograph
import turtle as t
t.colormode(255)
turtle.speed('fast')
def random_colour():
    r = random.randint(0, 255)        # will get random value from 0 to 255
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
def spirograph(change_in_angle):        # Set a parameter which i can assign to it after
    for movement in range(int(360/change_in_angle)):
        turtle.color(random_colour())
        turtle.circle(50)                  # circle with radius 50
        new_heading = turtle.heading() + change_in_angle  # turtle.heading() is initially 0, add 5 angle to every interation
        turtle.setheading(new_heading)
spirograph(5)        # Call function with parameter 

screen = Screen()     # Need to put these at the end of project in order to see the window,
screen.exitonclick()            # won't disappear until we click on it