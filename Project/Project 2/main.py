import turtle
from CONFIGS import *

def draw_tile(turtle, width, height, color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def ft_draw_map(turtle):
    # Draw the map
    for i in range(len(map)):
        for j in range(len(map[i])):
            t.goto(-(width/2)/10 * 9 + j*20, -(height/2)/10 * 9 - i*20 + height - height/10 - announcement_height - width/10/2)
            switcher = {
                0: "white",
                1: "grey",
                2: "yellow",
                3: "orange",
                4: "green",
            }
            key = map[i][j]
            color = switcher.get(int(key), "white")
            draw_tile(turtle, 20, 20, color)


def texte(turtle, text, size, color):
    turtle.color(color)
    turtle.write(text, font=("Arial", size, "normal"))

def player(turtle, size, color, coord):
    draw_tile(turtle, size, color)



#### MAIN ####
width = 600
height = 600
announcement_height = height / 10 * 1.5
inventory_width = width / 10 * 2

# Create the turtle
t = turtle.Turtle()
t.speed(0)
#t.hideturtle()
t.penup()
# Create the screen
s = turtle.Screen()
s.title("Python des Neiges") # Title of the window
s.bgcolor("white") # Set the background color
s.setup(width, height) # 480x480 pixels
s.tracer(0) # Disable the animation

# Store map
map = []
with open("plan_chateau.txt", "r") as f:
    for line in f:
        map.append(line.strip().split(" "))
# Draw the board
while (True):
    # Draw the announcement board
    t.goto(-(width/2)/10 * 9, height/2 - announcement_height - (width/2)/10)
    draw_tile(t, width - width/10, announcement_height, "#7e9873")

    # Draw the board
    t.goto(-(width/2)/10 * 9, -(height/2)/10 * 9)
    draw_tile(t, width - inventory_width - width/10 - width/10/2, height - height/10 - announcement_height - width/10/2, "#7e9873")
    t.goto(-(width/2)/10 * 9, -(height/2)/10 * 9)
    ft_draw_map(t)


    # Draw the inventory
    t.goto(width/2 - inventory_width - (width/2)/10, -(height/2)/10 * 9)
    draw_tile(t, inventory_width, height - height/10 - announcement_height - width/10/2, "#7e9873")
    print("update")
    s.update() # Update the screen

turtle.done()
