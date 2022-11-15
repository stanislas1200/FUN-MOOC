import turtle, random
from CONFIGS import *
from ast import literal_eval as make_tuple

dev = True


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


def ft_draw_castle_map():
    """Draw the entire castle_map and player"""
    t.goto(BOARD_COORD)
    draw_tile(BOARD_SIZE, COULEUR_BOX)
    for i in range(len(castle_map)):
        for j in range(len(castle_map[i])):
            t.goto(BOARD_COORD[0] + j * tile_size + text_center,
                   BOARD_COORD[1] - i * tile_size + BOARD_SIZE[1] - tile_size)
            switcher = {
                -7: "#387D41",
                -6: "white",
                -5: "red",
                -4: "#272C45",
                -3: "#124E8A",
                -1: COULEUR_VUE,
                0: COULEUR_CASES,
                1: COULEUR_MUR,
                2: COULEUR_OBJECTIF,
                3: COULEUR_PORTE,
                4: COULEUR_OBJET,
                -2: COULEUR_VUE
            }
            color = switcher.get(int(castle_map[i][j]), COULEUR_MISSING)
            draw_tile((tile_size, tile_size), color)
            if int(castle_map[i][j]) == -1:
                t.goto(BOARD_COORD[0] + j * tile_size + tile_size / 2 + text_center,
                       BOARD_COORD[1] - i * tile_size + BOARD_SIZE[1] - tile_size - player_size + tile_size / 2)
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
    t.goto(ANNOUNCEMENT_COORD)
    draw_tile(ANNOUNCEMENT_SIZE, COULEUR_BOX)
    t.color(color)
    t.goto(ANNOUNCEMENT_COORD[0] + ANNOUNCEMENT_SIZE[0] / 2,
           ANNOUNCEMENT_COORD[1] + ANNOUNCEMENT_SIZE[1] / 2 - text_size / 2)
    t.write(text, align="center", font=("Arial", int(text_size), "bold"))


# Inventory
def ft_inventory():
    """Draw the inventory"""
    t.goto(INVENTORY_COORD)
    draw_tile(INVENTORY_SIZE, COULEUR_BOX)
    t.goto(INVENTORY_COORD[0] + tile_size / 2, INVENTORY_COORD[1] + INVENTORY_SIZE[1] - tile_size)
    t.color(COULEUR_TEXTE)
    t.write("Inventory :", font=("Arial", int(INVENTORY_TEXT_SIZE), "bold"))
    for i in range(len(inventory)):
        t.goto(INVENTORY_COORD[0] + tile_size / 2, INVENTORY_COORD[1] + INVENTORY_SIZE[1] - tile_size -
               tile_size * (i + 1.5))
        t.write(f"N°{i}: {inventory[i]}", font=("Arial", int(INVENTORY_TEXT_SIZE / 1.5), "normal"))


# Function to update the player position on the castle_map
def ft_update_player(coord):
    """Update the player position on the castle_map"""
    global player_coord
    # Old player erasing
    castle_map[player_coord[0]][player_coord[1]] = -2
    t.goto(BOARD_COORD[0] + player_coord[1] * tile_size + text_center,
           BOARD_COORD[1] - player_coord[0] * tile_size + BOARD_SIZE[1] - tile_size)
    draw_tile((tile_size, tile_size), COULEUR_VUE)
    # New player coord
    player_coord = coord
    # New Tile player drawing
    castle_map[player_coord[0]][player_coord[1]] = -1
    t.goto(BOARD_COORD[0] + player_coord[1] * tile_size + text_center,
           BOARD_COORD[1] - player_coord[0] * tile_size + BOARD_SIZE[1] - tile_size)
    draw_tile((tile_size, tile_size), COULEUR_VUE)
    # Player drawing
    t.goto(BOARD_COORD[0] + player_coord[1] * tile_size + tile_size / 2 + text_center,
           BOARD_COORD[1] - player_coord[0] * tile_size + BOARD_SIZE[1] - tile_size - player_size + tile_size / 2)
    player(player_size, COULEUR_PERSONNAGE)
    # Update
    s.update()


# All events
def ft_check_tile(entity, coord):
    """Check if the tile is walkable or if there is an event"""
    global LEVEL_NUMBER, ee1, ee2
    ret = False
    if coord == (0, 1):
        ft_announcement("You Want leave the game ?", ANNOUNCEMENT_TEXT_SIZE / 1.5, COULEUR_TEXTE)
    if LEVEL_NUMBER == 1:
        if coord == (7, 15):
            ee1 = True
        elif coord == (12, 15):
            ee2 = True
    if castle_map[coord[0]][coord[1]] <= 0:
        ret = True
    elif entity == 0:
        if castle_map[coord[0]][coord[1]] == 3:
            ft_announcement("This door is close", ANNOUNCEMENT_TEXT_SIZE / 1.5, COULEUR_TEXTE)
            if dico_door[coord][1] == turtle.textinput("Door", dico_door[coord][0]):
                ret = True
                ft_announcement("Door open !", ANNOUNCEMENT_TEXT_SIZE / 1.5, COULEUR_TEXTE)
            else:
                ft_announcement("Wrong answerd", ANNOUNCEMENT_TEXT_SIZE / 1.5, COULEUR_TEXTE)
            turtle.listen()
        elif castle_map[coord[0]][coord[1]] == 4:
            ft_announcement(f"You found and object: {dico_objet[coord]}", ANNOUNCEMENT_TEXT_SIZE / 1.5, COULEUR_TEXTE)
            inventory.append(dico_objet[coord])
            ft_inventory()
            ret = True
        elif castle_map[coord[0]][coord[1]] == 2:
            # ft_update_player(coord)
            if LEVEL_NUMBER == 0:
                LEVEL_NUMBER = 1
                ft_announcement("Congratulation you think you won ?", ANNOUNCEMENT_TEXT_SIZE, COULEUR_TEXTE)
                ft_loading_level("plan_chateau2.txt", "dico_portes2.txt", "dico_objets2.txt")
            elif LEVEL_NUMBER == 1:
                if ee1 and ee2:
                    ee1 = ee2 = 0
                    ft_announcement("Whut what ?", ANNOUNCEMENT_TEXT_SIZE, COULEUR_TEXTE)
                    ft_loading_level("plan_chateau_bonus.txt", "dico_portes.txt", "dico_objets.txt")
                else:
                    ft_announcement("Congratulation you won !", ANNOUNCEMENT_TEXT_SIZE, COULEUR_TEXTE)
        elif dev and LEVEL_NUMBER == 0:
            ft_announcement(f"Tile {castle_map[coord[0]][coord[1]]}, x : {coord[1]}, y : {coord[0]}",
                            ANNOUNCEMENT_TEXT_SIZE / 1.5, COULEUR_TEXTE)
            ret = True
    return ret


def ft_loading_level(map_fd, dict_door_fd, dict_objet_fd):
    """Go to the next level"""
    global castle_map, dico_door, dico_objet, player_coord, inventory, tile_size, player_size, text_center, Enemy
    # Store castle_map
    castle_map = []
    # Store dico_objet
    dico_objet = {}
    # Store dico_door
    dico_door = {}
    # Loading the map
    with open(map_fd, "r") as f:
        for line in f:
            castle_map.append(line.strip().split(" "))
    castle_map = [[int(j) for j in i] for i in castle_map]
    # Loading the door
    with open(dict_door_fd, "r") as f:
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
    # Loading the object
    with open(dict_objet_fd, "r", ) as f:
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
    # Tile size
    tile_size = BOARD_SIZE[0] / len(castle_map[0]) if not BOARD_SIZE[0] / len(castle_map[0]) * len(castle_map) > \
                                                          BOARD_SIZE[1] else BOARD_SIZE[1] / len(castle_map)
    text_center = 0 if not BOARD_SIZE[0] / len(castle_map[0]) * len(castle_map) > BOARD_SIZE[1] \
        else (BOARD_SIZE[0] - tile_size * len(castle_map[0])) / 2
    # Player
    inventory = []
    player_size = (tile_size * RATIO_PERSONNAGE) / 2
    player_coord = POSITION_DEPART
    ft_inventory()
    ft_draw_castle_map()
    ft_update_player(player_coord)
    # enemy
    if LEVEL_NUMBER == 1:
        Enemy = [new_mob((12, 15), 1), new_mob((7, 15), 1)]
        turtle.ontimer(ft_enemie, 1000)


# Function to move
def ft_move_up():
    ft_update_player((player_coord[0] - 1, player_coord[1])) if ft_check_tile(0,
        (player_coord[0] - 1, player_coord[1])) else None


def ft_move_down():
    ft_update_player((player_coord[0] + 1, player_coord[1])) if ft_check_tile(0,
        (player_coord[0] + 1, player_coord[1])) else None


def ft_move_left():
    ft_update_player((player_coord[0], player_coord[1] - 1)) if ft_check_tile(0,
        (player_coord[0], player_coord[1] - 1)) else None


def ft_move_right():
    ft_update_player((player_coord[0], player_coord[1] + 1)) if ft_check_tile(0,
        (player_coord[0], player_coord[1] + 1)) else None


# Enemie
def ft_enemie():
    global Enemy
    for i in Enemy:
        i.move()
    turtle.ontimer(ft_enemie, 300)


class new_mob:
    def __init__(self, coord, direction):
        self.coord = coord
        self.direction = direction
        t.goto(BOARD_COORD[0] + self.coord[1] * tile_size + tile_size / 2 + text_center,
               BOARD_COORD[1] - self.coord[0] * tile_size + BOARD_SIZE[1] - tile_size - player_size + tile_size / 2)
        player(player_size, "red")

    def change_direction(self):
        self.temp = [0,1,2,3]
        switcher = {
            0: ft_check_tile(1, (self.coord[0], self.coord[1] + 1)),
            1: ft_check_tile(1, (self.coord[0], self.coord[1] - 1)),
            2: ft_check_tile(1, (self.coord[0] - 1, self.coord[1])),
            3: ft_check_tile(1, (self.coord[0] + 1, self.coord[1]))
        }
        ret = random.choice(self.temp)
        while self.temp:
            if switcher.get(ret) == False:
                self.temp.remove(ret)
                ret = random.choice(self.temp)
            else :
                print("New direction : ", ret)
                self.direction = ret
                break


    def move(self):
        global player_coord
        if self.coord[0] == player_coord[0] and self.coord[1] == player_coord[1]:
            ft_announcement("You died !", ANNOUNCEMENT_TEXT_SIZE, COULEUR_TEXTE)
            player_coord = POSITION_DEPART
        self.change_direction() if random.randint(0, 100) < 40 else None
        t.goto(BOARD_COORD[0] + self.coord[1] * tile_size + text_center,
               BOARD_COORD[1] - self.coord[0] * tile_size + BOARD_SIZE[1] - tile_size)
        switcher = {
            -1: COULEUR_VUE,
            0: COULEUR_CASES,
        }
        color = switcher.get(int(castle_map[self.coord[0]][self.coord[1]]), COULEUR_MISSING)
        draw_tile((tile_size, tile_size), color)
        if self.direction == 0:  # Right
            if ft_check_tile(1, (self.coord[0], self.coord[1] + 1)):
                self.coord = (self.coord[0], self.coord[1] + 1)
            else:
                self.direction = random.randint(0, 3)
        elif self.direction == 1:  # Left
            if ft_check_tile(1, (self.coord[0], self.coord[1] - 1)):
                self.coord = (self.coord[0], self.coord[1] - 1)
            else:
                self.direction = random.randint(0, 3)
        elif self.direction == 2:  # Up
            if ft_check_tile(1, (self.coord[0] - 1, self.coord[1])):
                self.coord = (self.coord[0] - 1, self.coord[1])
            else:
                self.direction = random.randint(0, 3)
        elif self.direction == 3:  # Down
            if ft_check_tile(1, (self.coord[0] + 1, self.coord[1])):
                self.coord = (self.coord[0] + 1, self.coord[1])
            else:
                self.direction = random.randint(0, 3)
        t.goto(BOARD_COORD[0] + self.coord[1] * tile_size + tile_size / 2 + text_center,
               BOARD_COORD[1] - self.coord[0] * tile_size + BOARD_SIZE[1] - tile_size - player_size + tile_size / 2)
        player(player_size, "red")


# Inventory array
inventory = []

# Create the turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

# Create the screen
s = turtle.Screen()
s.title("Python des Neiges")  # Title of the window
s.bgcolor(COULEUR_EXTERIEUR)  # Set the background color
s.setup(WINDOW_SIZE[0], WINDOW_SIZE[1])  # 480x555 pixels
s.tracer(0)  # Disable the animation

# Set keyboard bindings
turtle.listen()
turtle.onkeypress(ft_move_up, "Up")
turtle.onkeypress(ft_move_down, "Down")
turtle.onkeypress(ft_move_left, "Left")
turtle.onkeypress(ft_move_right, "Right")

if dev:
    turtle.onkey(s.bye, "q")
    Enemy = []
ee1 = ee2 = False

# Draw all one time
ft_loading_level("plan_chateau.txt", "dico_portes.txt", "dico_objets.txt")
ft_announcement("Welcome to the game", ANNOUNCEMENT_TEXT_SIZE, COULEUR_TEXTE)
turtle.mainloop()
turtle.done()
