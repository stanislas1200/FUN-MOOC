import random

def create_map(size, trapsNbr):
    """Create a map of size x size with trapsNbr traps"""
    MY_PRECIOUS = 1
    TRAP = -1
    my_map = {}
    while trapsNbr:
        x = random.randint(1, size)
        y = random.randint(1, size)
        if (x, y) not in my_map:
            my_map[(x, y)] = TRAP
            trapsNbr -= 1
    while True:
        x = random.randint(1, size)
        y = random.randint(1, size)
        if (x, y) not in my_map:
            my_map[(x, y)] = MY_PRECIOUS
            return my_map

def play_game(map_size, treasure_map):
    """Ask player to choose a position and return True if he found the treasure"""
    while True:
        inp = input().split()
        if (len(inp) == 2) and inp[0].isdigit() and inp[1].isdigit():
            x, y = int(inp[0]), int(inp[1])
            if x in range(1, map_size+1) and y in range(1, map_size+1):
                if (x, y) in treasure_map:
                    if treasure_map[(x, y)] == 1:
                        return True
                    else:
                        return False