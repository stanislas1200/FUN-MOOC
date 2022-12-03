import sys
from operator import itemgetter
from random import randint

""" Bug:

-| Can't go above 99
-| No input


"""


def rgb(r, g, b): return f"\u001b[38;2;{r};{g};{b}m"


def init_grid(width, height, nb_mines, grid):
    """Init the grid with x mines randomly on the board and returns the grid"""
    while nb_mines > 0:
        x = randint(0, width - 1)
        y = randint(0, height - 1)
        if grid[y][x] == 0:
            grid[y][x] = 9
            nb_mines -= 1
    return grid


def print_grid(width, height, grid):
    """Prints the grid"""
    biggest_y_number = len(str(height))
    biggest_x_number = len(str(width))
    # Print x-axis
    for i in range(biggest_x_number):
        print(" " * (biggest_y_number + 1), end="")
        for x in range(width):
            x = str(x)
            print(" " + (x[-i] if len(x) > 1 or i == biggest_x_number - 1 else " "), end=" ")
        print()

    # Top border
    print(" " * (biggest_y_number + 1), end="")
    print("———" * width)

    # Print y-axis and grid
    for y in range(height):
        # Print y number and left border
        print(str(y).rjust(biggest_y_number), end="|")
        for x in range(width):
            print((rgb(255, 0, 0) if grid[y][x] == 9 else rgb(255, 255, 255)) + " " + str(grid[y][x])
                  + rgb(255, 255, 255), end=" ")
        # Right border
        print("|")

    # Bottom border
    print(" " * (biggest_y_number + 1), end="")
    print("———" * width)


class check:
    def args(argv):
        """Check args"""
        error = 0
        print(rgb(189, 0, 0), end="")
        if len(argv) != 4:
            print("Usage: python3 demineur.py <width> <height> <nb_mines>")
            error = 1
        if (not argv[1].isdigit()) or (not argv[2].isdigit()) or (not argv[3].isdigit()):
            print("Error: width, height and nb_mines must be integers")
            error = 1
        if (int(argv[1]) < 1) or (int(argv[2]) < 1) or (int(argv[3]) < 1):
            print("Error: width, height and nb_mines must be positive")
            error = 1
        if int(argv[3]) >= int(argv[1]) * int(argv[2]):
            print("Error: too many mines")
            error = 1
        print(rgb(255, 255, 255), end="")
        return error

    def input(x, y, width, height):
        """Check input"""
        error = 0
        print(rgb(189, 0, 0), end="")
        if not x.isdigit() or not y.isdigit():
            print("Error: x and y must be integers")
            error = 1
        elif (int(x) < 0) or (int(y) < 0):
            print("Error: x and y must be positive")
            error = 1
        elif (int(x) >= width) or (int(y) >= height):
            print("Error: x and y must be in the grid")
            error = 1
        print(rgb(255, 255, 255), end="")
        return error


def start_game(width, height, reference_board, game_board):
    """Start the game"""
    while True:
        #print_grid(width, height, reference_board)
        print_grid(width, height, game_board)
        x, y = input("x y: ").split()
        if not check.input(x, y, width, height):
            if reference_board[int(y)][int(x)] == 9:
                print("Game over")
                break
            else:
                game_board[int(y)][int(x)] = reference_board[int(y)][int(x)]


def main(argv):
    exit(1) if check.args(argv) == 1 else None
    # Init data
    data = {
        "width": int(argv[1]),
        "height": int(argv[2]),
        "nb_mines": int(argv[3]),
        "reference_board": [[0] * int(argv[1]) for i in range(int(argv[2]))],
        "game_board": [["."] * int(argv[1]) for i in range(int(argv[2]))],
    }
    # Init grid with mines
    data["reference_board"] = init_grid(*itemgetter("width", "height", "nb_mines", "reference_board")(data))
    print("width: " + str(data["width"]), "height: " + str(data["height"]), "mines: " + str(data["nb_mines"]), sep="\t")
    start_game(*itemgetter("width", "height", "reference_board", "game_board")(data))
    # print_grid(*itemgetter("width", "height", "reference_board")(data))
    # print_grid(*itemgetter("width", "height", "game_board")(data))


if __name__ == "__main__":
    main(sys.argv)
