"""
Prenom : Stanislas
Nom : Godin
Matricule : 000575477
Section : B1-INFO
"""

import sys
from random import randint


""" Bug:
-| Slow on 2000x2000
-| Seg fault on python3 demineur.py 20 1500 50
-| Unknown test cuz lambda missing x argument
"""


def rgb(r, g, b): return f"\u001b[38;2;{r};{g};{b}m"


def create_board(n, m):
    """Create a board and return it Useless function"""
    return [['.'] * n for i in range(m)]


def get_size(board):
    """Returns the size of the board Useless function"""
    return len(board[0]), len(board)


def get_neighbours(x, y):
    """Get the neighbours of a cell"""
    ret = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                ret.append((x + i, y + j))
    return ret


def place_mines(reference_board, number_of_mines, first_pos_x, first_pos_y):
    """Place the mines on the board"""
    # Get the size of the board
    width, height = get_size(reference_board)
    # Create an empty list
    ret = []
    # Place the mines while there are still mines to place
    while number_of_mines > 0:
        # Get a random position
        x = randint(0, width - 1)
        y = randint(0, height - 1)
        # If the position is not already a mine and is not the first click or neighbours of the first click
        if reference_board[y][x] != 9 and (x, y) not in get_neighbours(first_pos_x, first_pos_y)\
                and (x, y) != (first_pos_x, first_pos_y):
            # Place the mine on the board
            reference_board[y][x] = 9
            # Add the position to the list
            ret.append([x, y])
            # Remove a mine from the number of mines to place
            number_of_mines -= 1
    # Return the list of mines
    return ret


def get_mines_around(reference_board, pos_x, pos_y):
    """Get the number of mines around"""
    # Make a variable to store the number of mines
    mines = 0
    # For each cell around
    for i in range(-1, 2):
        for j in range(-1, 2):
            # If the position is valid
            if 0 <= pos_x + i < len(reference_board[0]) and 0 <= pos_y + j < len(reference_board):
                # If the cell is a mine
                if reference_board[pos_y + j][pos_x + i] == 9:
                    # Add a mine to the number of mines
                    mines += 1
    # Return the number of mines
    return mines


def fill_in_board(reference_board):
    """Fill in the board with the number of mines around"""
    # Get the size of the board
    width, height = get_size(reference_board)
    # For each cell
    for y in range(height):
        for x in range(width):
            # If the position is not a mine
            if reference_board[y][x] != 9:
                # Get the number of mines around
                reference_board[y][x] = get_mines_around(reference_board, x, y)


def propagate_click(game_board, reference_board, pos_x, pos_y):
    """Propagate the click"""
    # If the position is an empty cell
    if game_board[pos_y][pos_x] == '.' or game_board[pos_y][pos_x] == 'F':
        # Update the game board
        game_board[pos_y][pos_x] = reference_board[pos_y][pos_x]
        # If the position is an 0
        if reference_board[pos_y][pos_x] == 0:
            # For each cell around
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # If the position is valid
                    if 0 <= pos_x + i < len(game_board[0]) and 0 <= pos_y + j < len(game_board):
                        # Propagate the click
                        propagate_click(game_board, reference_board, pos_x + i, pos_y + j)


def parse_input(n, m):
    """Parse the input"""
    # Ask for the input
    print("Enter the coordinates of the cell you want to click and the type ([c/f] x y):", end=" ")
    # Get the input
    inp = input()
    # Check if the input is valid
    ret = check.input(inp, n, m)
    # Return the input if it is valid
    return ret if ret else parse_input(n, m)


def check_win(game_board, reference_board, mine_list, total_flags):
    """Check if the game is won"""
    # Get the size of the board
    width, height = get_size(game_board)
    undisclosed_cells = 0
    # For each cell
    for y in range(height):
        for x in range(width):
            # If the cell is not revealed
            if game_board[y][x] == '.' or game_board[y][x] == 'F':
                undisclosed_cells += 1
    # If the number of undisclosed cells is equal to the number of mines
    if undisclosed_cells == len(mine_list):
        return True
    # If the number of flags is equal to the number of mines
    if total_flags == len(mine_list):
        # if all the mines are flagged
        for i in mine_list:
            # If a mine is not flagged
            if game_board[i[1]][i[0]] != 'F':
                return False
        return True
    return False


def init_game(n, m, number_of_mines):
    """Init the game"""
    # Create the board
    reference_board = create_board(n, m)
    # Print the board
    print_board(reference_board)
    # Ask for the first click
    cell, x, y = parse_input(n, m)
    # Place the mines
    mine_list = place_mines(reference_board, number_of_mines, x, y)
    # Fill in the reference board
    fill_in_board(reference_board)
    # Create the game board
    game_board = create_board(n, m)
    # Propagate the first click
    propagate_click(game_board, reference_board, x, y)
    # Return the 2 boards and the mine list
    return game_board, reference_board, mine_list


def print_board(board):
    """Prints the board"""
    # Get the size of the board
    width, height = get_size(board)
    # Get the max number of digits
    biggest_y_number = len(str(height))
    biggest_x_number = len(str(width))
    # Print x-axis
    for i in range(biggest_x_number, 0, -1):
        # Print the first space
        print(" " * (biggest_y_number + 1), end="")
        # Print the numbers
        for x in range(width):
            x = str(x)
            print(" " + (x[-i] if len(x) >= i else " "), end=" ")
        # Print a new line
        print()

    # Print top border
    print(" " * (biggest_y_number + 1) + "———" * width)

    # Print y-axis and grid
    for y in range(height):
        # Print y number and left border
        print(str(y).rjust(biggest_y_number), end="|")
        for x in range(width):
            if board[y][x] == 9:
                print(rgb(255, 0, 0) + " x" + rgb(255, 255, 255), end=" ")
            elif board[y][x] == "F":
                print(rgb(0, 255, 0) + " F" + rgb(255, 255, 255), end=" ")
            else:
                print(" " + str(board[y][x]), end=" ")
        # print right border
        print("|")

    # Print bottom border
    print(" " * (biggest_y_number + 1) + "———" * width)


class check:
    @staticmethod
    def args(argv):
        """Check args"""
        error = 0
        # Color the error message
        print(rgb(189, 0, 0), end="")
        # If the number of arguments is not 3
        if len(argv) != 4:
            print("Usage: python3 demineur.py <width> <height> <nb_mines>")
            error = 1
        elif (not argv[1].isdigit()) or (not argv[2].isdigit()) or (not argv[3].isdigit()):
            print("Error: width, height and nb_mines must be integers and positive")
            error = 1
        elif (int(argv[1]) < 4) or (int(argv[2]) < 4) or (int(argv[3]) < 1):
            print("Error: width, height must be greater than 3 and nb_mines must be greater than 0")
            error = 1
        elif (int(argv[1]) > 1200 or int(argv[2]) > 1200):
            print("Error: width and height must be less than 1200, otherwise the game will be too slow and u need a big screen °~° also it can overflow")
            error = 1
        elif int(argv[3]) >= int(argv[1]) * int(argv[2]) - 1:
            print("Error: too many mines")
            error = 1
        # Reset the color
        print(rgb(255, 255, 255), end="")
        # Return the error code
        return error

    @staticmethod
    def input(inp, width, height):
        """Check input"""
        error = 0
        cell = x = y = None
        # Color the error message
        print(rgb(189, 0, 0), end="")
        # If no input or not 3 arguments
        if not inp or len(inp.split()) != 3:
            print("Error: invalid input length")
            error = 1
        else:
            # Split the input
            cell, x, y = inp.split()
            # If the cell is not c or f
            if cell not in ["c", "f"]:
                print("Error: action type must be c or f")
                error = 1
            # If the x or y is not an integer or is not positive
            if not x.isdigit() or not y.isdigit():
                print("Error: x and y must be integers and positive")
                error = 1
            # If the x or y is out of the board
            elif (int(x) >= width) or (int(y) >= height):
                print("Error: x and y must be in the board")
                error = 1
        # Reset the color
        print(rgb(255, 255, 255), end="")
        # Return the input if valid or None if not
        return (cell, int(x), int(y)) if not error else None


def main():
    argv = sys.argv
    # Check the arguments
    exit(0) if check.args(argv) == 1 else None
    if (int(argv[1]) * int(argv[2])) > 1000:
        sys.setrecursionlimit(int(argv[1]) * int(argv[2]))
    # Init the game
    game_board, reference_board, mine_list = init_game(int(argv[1]), int(argv[2]), int(argv[3]))
    """Start the game"""
    # Get the size of the board
    width, height = get_size(game_board)
    total_flags = 0
    # Print the board
    print_board(game_board)
    # Check if the game is won
    if check_win(game_board, reference_board, mine_list, total_flags=0):
        # Print that the player won then exit
        print(rgb(0, 255, 0) + "You won!" + rgb(255, 255, 255))
        return 1
    # While the game is not won or lost
    while True:
        # Ask for the next click
        cell, x, y = parse_input(width, height)
        # If the position is a mine and the cell is a not flag
        if [x, y] in mine_list and cell == 'c':
            # Print the reference_board and that the player lost then exit
            print_board(reference_board)
            print(rgb(255, 0, 0) + "You lost!" + rgb(255, 255, 255))
            return 0
        else:
            # If the cell is a flag
            if cell == 'f':
                # If the cell is not flagged
                if game_board[y][x] == '.':
                    # Flag the cell
                    game_board[y][x] = 'F'
                    total_flags += 1
                # If the cell is flagged
                elif game_board[y][x] == 'F':
                    # Unflag the cell
                    game_board[y][x] = '.'
                    total_flags -= 1
                else:
                    print(rgb(255, 255, 0) + "You can't flag a revealed cell!" + rgb(255, 255, 255))
            else:
                # Propagate the click
                propagate_click(game_board, reference_board, x, y)
            # Print the board
            print_board(game_board)
            # If the game is won
            if check_win(game_board, reference_board, mine_list, total_flags):
                # Print that the player won then exit
                print(rgb(0, 255, 0) + "You won!" + rgb(255, 255, 255))
                return 1


if __name__ == "__main__":
    main()
