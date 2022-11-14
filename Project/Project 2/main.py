import turtle
from CONFIGS import *
from ast import literal_eval as make_tuple

dev = False


def draw_tile(box_size, color):
    """Draw a box"""
    t.color(color)
    t.begin_fill()
    for i in range(2):
        t.forward(box_size[0])
        t.left(90)
        t.forward(box_size[1])
        t.left(90)
    t.end_fill()


def ft_draw_map(tile_size):
    """Draw the entire map and player"""
    for i in range(len(map)):
        for j in range(len(map[i])):
            t.goto(board[0] + j * tile_size + map_center,
                   board[1] - i * tile_size + board_size[1] - tile_size)
            switcher = {
                -1: COULEUR_VUE,
                0: COULEUR_CASES,
                1: COULEUR_MUR,
                2: COULEUR_OBJECTIF,
                3: COULEUR_PORTE,
                4: COULEUR_OBJET,
                -2: COULEUR_VUE
            }
            color = switcher.get(int(map[i][j]), COULEUR_MISSING)
            draw_tile((tile_size, tile_size), color)
            if dev:
                t.color("black")
                t.write(map[i][j], font=("Arial", 10, "normal"))
                # turtle.color("blue")
                # turtle.write((i, j), font=("Arial", 10, "normal"))
            if int(map[i][j]) == -1:
                t.goto(board[0] + j * tile_size + tile_size / 2 + map_center,
                       board[1] - i * tile_size + board_size[1] - tile_size - player_size + tile_size / 2)
                player(player_size, COULEUR_PERSONNAGE)
    s.update()


def player(size, color):
    """Draw the player"""
    t.color(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()


def ft_announcement(text, text_size, color):
    """Draw an announcement on the screen"""
    t.goto(announcement_coord)
    draw_tile(announcement_size, COULEUR_BOX)
    t.color(color)
    t.goto(announcement_coord[0] + announcement_size[0] / 2,
           announcement_coord[1] + announcement_size[1] / 2 - text_size / 2)
    t.write(text, align="center", font=("Arial", int(text_size), "bold"))


# Inventory
def ft_inventory():
    t.goto(inventory_coord)
    draw_tile(inventory_size, COULEUR_BOX)
    t.goto(inventory_coord[0] + size / 2, inventory_coord[1] + inventory_size[1] - size)
    t.color(COULEUR_TEXTE)
    t.write("Inventory :", font=("Arial", int(INVENTORY_TEXT_SIZE), "bold"))
    for i in range(len(inventory)):
        t.goto(inventory_coord[0] + size / 2, inventory_coord[1] + inventory_size[1] - size - size * (i + 1.5))
        t.write(f"N°{i}: {inventory[i]}", font=("Arial", int(INVENTORY_TEXT_SIZE / 1.5), "normal"))


# Function to update the player position on the map
def ft_update_player(coord):
    global player_coord
    # Old player erasing
    map[player_coord[0]][player_coord[1]] = -2
    t.goto(board[0] + player_coord[1] * size + map_center,
           board[1] - player_coord[0] * size + board_size[1] - size)
    draw_tile((size, size), COULEUR_VUE)
    # New player coord
    player_coord = coord
    # New Tile player drawing
    map[player_coord[0]][player_coord[1]] = -1
    t.goto(board[0] + player_coord[1] * size + map_center,
           board[1] - player_coord[0] * size + board_size[1] - size)
    draw_tile((size, size), COULEUR_VUE)
    # Player drawing
    t.goto(board[0] + player_coord[1] * size + size / 2 + map_center,
           board[1] - player_coord[0] * size + board_size[1] - size - player_size + size / 2)
    player(player_size, COULEUR_PERSONNAGE)
    # Update
    s.update()


# All events
def ft_check_tile(coord):
    """Check if the tile is walkable or if there is an event"""
    if coord == (0, 1):
        ft_announcement("You Want leave the game ?", ANNOUNCEMENT_TEXT_SIZE / 1.5, COULEUR_TEXTE)
    if dev:
        ft_update_player(coord)
    if map[coord[0]][coord[1]] <= 0:
        ft_update_player(coord)
    elif map[coord[0]][coord[1]] == 3:
        ft_announcement("This door is close", ANNOUNCEMENT_TEXT_SIZE / 1.5, COULEUR_TEXTE)
        if dico_door[coord][1] == turtle.textinput("Door", dico_door[coord][0]):
            ft_update_player(coord)
            ft_announcement("Door open", ANNOUNCEMENT_TEXT_SIZE / 1.5, COULEUR_TEXTE)
        turtle.listen()
    elif map[coord[0]][coord[1]] == 4:
        inventory.append(dico_objet[coord])
        ft_inventory()
        ft_update_player(coord)
    elif map[coord[0]][coord[1]] == 2:
        ft_update_player(coord)
        ft_announcement(t, "You are on a chest", ANNOUNCEMENT_TEXT_SIZE / 1.5, COULEUR_TEXTE)


# Function to move
def ft_move_up():
    ft_check_tile((player_coord[0] - 1, player_coord[1]))


def ft_move_down():
    ft_check_tile((player_coord[0] + 1, player_coord[1]))


def ft_move_left():
    ft_check_tile((player_coord[0], player_coord[1] - 1))


def ft_move_right():
    ft_check_tile((player_coord[0], player_coord[1] + 1))


#### MAIN ####
width = WINDWOS_SIZE[0]
height = WINDWOS_SIZE[1]

# Announcement
announcement_size = ANNOUNCEMENT_SIZE
announcement_coord = ANNOUNCEMENT_COORD

# Inventory
inventory_size = INVENTORY_SIZE
inventory_coord = INVENTORY_COORD
inventory = []

# Board
board = BOARD_COORD
board_size = BOARD_SIZE

# Create the turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

# Create the screen
s = turtle.Screen()
s.title("Python des Neiges")  # Title of the window
s.bgcolor("white")  # Set the background color
s.setup(width, height)  # 480x480 pixels
s.tracer(0)  # Disable the animation

# Store map
map = []
with open("plan_chateau.txt", "r") as f:
    for line in f:
        map.append(line.strip().split(" "))
map = [[int(j) for j in i] for i in map]

# Store dico_objet
dico_objet = {}
with open("dico_objets.txt", "r", ) as f:
    for line in f:
        coord_done = 0
        x = ""
        y = ""
        for i in range(len(line)):
            if line[i].isdigit() and coord_done == 0:
                x += line[i]
            elif line[i].isdigit() and coord_done == 1:
                y += line[i]
            if line[i] == ",":
                coord_done += 1
            if coord_done == 2:
                dico_objet[(int(x), int(y))] = line[i + 2:]
                break

# Store dico_door
dico_door = {}
with open("dico_portes.txt", "r") as f:
    for line in f:
        coord_done = 0
        x = ""
        y = ""
        for i in range(len(line)):
            if line[i].isdigit() and coord_done == 0:
                x += line[i]
            elif line[i].isdigit() and coord_done == 1:
                y += line[i]
            if line[i] == ",":
                coord_done += 1
            if coord_done == 2:
                dico_door[(int(x), int(y))] = make_tuple(line[i + 2:])
                break
# Tile size
size = board_size[0] / len(map[0]) if not board_size[0] / len(map[0]) * len(map) > board_size[1] \
    else board_size[1] / len(map)
map_center = 0 if not board_size[0] / len(map[0]) * len(map) > board_size[1] \
    else (board_size[0] - size * len(map[0])) / 2

# Player
player_size = size * RATIO_PERSONNAGE / 2
player_coord = (0, 1)

# Set keyboard bindings
turtle.listen()
turtle.onkeypress(ft_move_up, "Up")
turtle.onkeypress(ft_move_down, "Down")
turtle.onkeypress(ft_move_left, "Left")
turtle.onkeypress(ft_move_right, "Right")

if dev:
    turtle.onkey(s.bye, "Escape")

# Draw the board one time
t.goto(board)
draw_tile(board_size, COULEUR_BOX)
ft_draw_map(size)
ft_inventory()
ft_announcement("Welcome to the game", ANNOUNCEMENT_TEXT_SIZE, COULEUR_TEXTE)

# Draw the board Don't need
turtle.mainloop()
turtle.done()
