import turtle
from CONFIGS import *
import keyboard


def draw_tile(turtle, size, color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(size[0])
        turtle.left(90)
        turtle.forward(size[1])
        turtle.left(90)
    turtle.end_fill()

def ft_draw_map(turtle, size):
    # Draw the map
    if size * len(map) > height - height/10 - announcement_size[1] - width/10/2:
        size = (height - height/10 - announcement_size[1] - width/10/2) / len(map)
    for i in range(len(map)):
        for j in range(len(map[i])):
            t.goto(board[0] + j*size, board[1] - i*size + height - height/10 - announcement_size[1] - width/10/2 - size)
            switcher = {
                -1: "white",
                0: "white",
                1: "grey",
                2: "yellow",
                3: "orange",
                4: "green",
                5: "wheat"
            }
            color = switcher.get(int(map[i][j]), "white")
            draw_tile(turtle, (size, size), color)
            if (int(map[i][j]) == -1):
                t.goto(board[0] + j*size + size/2, board[1] - i*size + height - height/10 - announcement_size[1] - width/10/2 - size - player_size + size/2)
                player(turtle, player_size, "red")
    print("Map drawn")
    s.update()


def texte(turtle, text, size, color):
    turtle.color(color)
    turtle.write(text, font=("Arial", size, "normal"))

def player(turtle, size, color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()


def ft_move_up():
    print("up")
    global player_coord
    map[player_coord[0]][player_coord[1]] = 5
    player_coord = (player_coord[0] - 1, player_coord[1])
    map[player_coord[0]][player_coord[1]] = -1
    t.goto(-(width / 2) / 10 * 9, -(height / 2) / 10 * 9)
    ft_draw_map(t, size)
def ft_move_down():
    print("down")
    global player_coord
    map[player_coord[0]][player_coord[1]] = 5
    player_coord = (player_coord[0] + 1, player_coord[1])
    map[player_coord[0]][player_coord[1]] = -1
    t.goto(-(width / 2) / 10 * 9, -(height / 2) / 10 * 9)
    ft_draw_map(t, size)
def ft_move_left():
    print("left")
    global player_coord
    map[player_coord[0]][player_coord[1]] = 5
    player_coord = (player_coord[0], player_coord[1] - 1)
    map[player_coord[0]][player_coord[1]] = -1
    t.goto(-(width / 2) / 10 * 9, -(height / 2) / 10 * 9)
    ft_draw_map(t, size)
def ft_move_right():
    print("right")
    global player_coord
    map[player_coord[0]][player_coord[1]] = 5
    player_coord = (player_coord[0], player_coord[1] + 1)
    map[player_coord[0]][player_coord[1]] = -1
    t.goto(-(width / 2) / 10 * 9, -(height / 2) / 10 * 9)
    ft_draw_map(t, size)


#### MAIN ####
width = 580
height = 780
# Announcement
announcement_size = (width - width/10, height / 10 * 1.5)
announcement_coord = (-(width/2)/10 * 9, height/2 - announcement_size[1] - (width/2)/10)
# Inventory
inventory_size = (width / 10 * 2, height - height/10 - announcement_size[1] - width/10/2)
inventory_coord = (width/2 - inventory_size[0] - (width/2)/10, -(height/2)/10 * 9)
# Board
board = (-(width/2)/10 * 9, -(height/2)/10 * 9)
board_size = (width - inventory_size[0] - width/10 - width/10/2, height - height/10 - announcement_size[1] - width/10/2)


# Create the turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
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

size = (width - inventory_size[0] - width/10 - width/10/2) / len(map[0])
# Player
player_size = size * RATIO_PERSONNAGE / 2
player_coord = (0, 1)


# Set keyboard bindings
turtle.listen()
turtle.onkey(ft_move_up, "Up")
turtle.onkey(ft_move_down, "Down")
turtle.onkey(ft_move_left, "Left")
turtle.onkey(ft_move_right, "Right")


# Draw the board one time
t.goto(board)
draw_tile(t, board_size, "#7e9873")
t.goto(-(width / 2) / 10 * 9, -(height / 2) / 10 * 9)
ft_draw_map(t, size)

# Draw the board Don't need
while (True):
    # Draw the announcement board
    t.goto(announcement_coord)
    draw_tile(t, announcement_size, "#7e9873")


    # Draw the player

    # Draw the inventory
    t.goto(inventory_coord)
    draw_tile(t, inventory_size, "#7e9873")

    s.update() # Update the screen

turtle.done()
