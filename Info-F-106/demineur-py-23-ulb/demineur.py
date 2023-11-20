import sys
import os
import random

clear = "\x1b[H\x1b[2J"
bold = "\x1b[1m"
error = 0
cases_to_find = 0

def rgb(r, g, b): return f"\u001b[38;2;{r};{g};{b}m"

def read_bombes(path):
	"""Reads the bombes file and returns a list of bombes"""
	if not os.path.isfile(path):
		print(clear + rgb(255,0,0) + "Error: " + rgb(220,230,0) + f"File does not exist: {rgb(255,255,255)} {path}")
		return exit(1)
	with open(path, "r") as f:
		lines = f.readlines()
		tuple_bombes = {tuple(map(int, line.strip().split(","))): "B" for line in lines}
	return tuple_bombes

def check_input(inp, board):
	"""Check if the input is correct"""
	global error
	if (not inp.isdigit()):
		print(clear + rgb(255,0,0) + "Error: " + rgb(255,255,255) + "Input must be a number!")
		error = 1
		return False
	inp = int(inp)
	if (inp < 0 or inp >= len(board)):
		print(clear + rgb(255,0,0) + "Error: " + rgb(255,255,255) + "Input must be between 0 and " + str(len(board)-1) + "!")
		error = 1
		return False
	return True


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
	width, height = len(reference_board[0]), len(reference_board)
	# For each cell
	for y in range(height):
		for x in range(width):
			# If the position is not a mine
			if reference_board[y][x] != 9:
				# Get the number of mines around
				reference_board[y][x] = get_mines_around(reference_board, x, y)

def propagate_click(board, reference_board, pos_y, pos_x):
	"""Propagate the click"""
	# check if empty
	if (board[pos_y][pos_x] != "."): return
	board[pos_y][pos_x] = reference_board[pos_y][pos_x]
	if (board[pos_y][pos_x] == 0):
		for i in range(-1, 2):
			for j in range(-1, 2):
				if (0 <= pos_x + i < len(board[0]) and 0 <= pos_y + j < len(board)):
					propagate_click(board, reference_board, pos_y + j, pos_x + i)

def place_mine(board, bombes):
	"""Place the bombes"""
	for pos in bombes:
		board[pos[0]][pos[1]] = 9

def get_cases_left(board, bombes_nb):
	"""Get the number of cases left"""
	cases = 0
	for line in board:
		for case in line:
			if (case == "."):
				cases += 1
	return cases - bombes_nb

def play(board, bombes, diff):
	"""Play the game"""
	global cases_to_find
	round = 0
	reference_board = create_board(len(board))
	place_mine(reference_board, bombes.keys())
	fill_in_board(reference_board)
	while (1):
		print_board(board)
		print("### Round " + str(round))
		cases_to_find = get_cases_left(board, len(bombes))
		print("--- Cases to find: " + str(cases_to_find) + " ---")
		print("Choose your line " + rgb(255,255,255) + "(0-" + str(len(board)-1) + ")")
		line = input()
		if (not check_input(line, board)): continue
		print("Choose your column " + rgb(255,255,255) + "(0-" + str(len(board)-1) + ")")
		column = input()
		if (not check_input(column, board)): continue
		round += 1
		if ((int(line), int(column)) in bombes):
			print(rgb(255,0,0) + "You lost")
			break
		else:
			propagate_click(board, reference_board, int(line), int(column))
		# print_board(board)
		if check_win(board, bombes):
			# Print that the player won then exit
			print_board(board)
			print(rgb(0, 255, 0) + "You won!" + rgb(255, 255, 255))
			exit(1)
		if (diff == 2):
			bombes = make_mine_dict(int(len(board) * len(board) / 5), board)
			reference_board = create_board(len(board))
			place_mine(reference_board, bombes.keys())
			fill_in_board(reference_board)
			new_board = create_board(len(board))
			for i in range(len(board)):
				for j in range(len(board)):
					if (board[i][j] == "."):
						new_board[i][j] = "."
					else:
						propagate_click(new_board, reference_board, i, j)
			board = new_board

def make_mine_dict(n, board):
	"""Make a dictionary of bombs"""
	mine_dict = {}
	nb_mines = 0
	size = len(board)
	while nb_mines < n:
		x = random.randint(0, size - 1)
		y = random.randint(0, size - 1)
		if (x, y) not in mine_dict and board[x][y] == "." and (x, y) != (0, 0) and (x, y) != (size - 1, size - 1) and (x, y) != (0, size - 1) and (x, y) != (size - 1, 0):
			mine_dict[(x, y)] = "B"
			nb_mines += 1
	return mine_dict


def ask_size(diff):
	global cases_to_find
	while (1):
		print(rgb(255,255,255) + "Choose a size: ")
		n = input()
		if (n.isdigit()):
			nb = int(n)
			board = create_board(nb)
			bombes = make_mine_dict(int(nb * nb / 5), board)
			# sys.setrecursionlimit(nb * nb)
			cases_to_find = nb * nb - len(bombes)
			break
		else:
			print(rgb(255,0,0) + "Size must be a number !")
	play(board, bombes, diff)
		
def facile():
	global cases_to_find
	board = create_board(9)
	bombes = read_bombes("bombes.txt")
	cases_to_find = len(board) * len(board) - len(bombes)
	play(board, bombes, 0)

def moyen():
	ask_size(1)

def difficile():
	ask_size(2)

def check_win(game_board, mine_list):
	"""Check if the game is won"""
	# Get the size of the board
	width, height = len(game_board[0]), len(game_board)
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
	return False


def print_board(board):
	"""Prints the board"""
	global error
	if (not error):
		print(clear)
	error = 0
	# Get the size of the board
	width, height = len(board[0]), len(board)
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
			elif board[y][x] == 0:
				print("  ", end=" ")
			else:
				print(" " + str(board[y][x]), end=" ")
		# print right border
		print("|")

	# Print bottom border
	print(" " * (biggest_y_number + 1) + "———" * width)


def create_board(n):
	"""Create a square board and return it"""
	return [['.'] * n for _ in range(n)]


def main():
	print(clear)
	print(bold + rgb(31,226,70))
	print("███╗   ███╗██╗███╗   ██╗███████╗███████╗██╗    ██╗███████╗███████╗██████╗ ███████╗██████╗ ")
	print("████╗ ████║██║████╗  ██║██╔════╝██╔════╝██║    ██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗")
	print("██╔████╔██║██║██╔██╗ ██║█████╗  ███████╗██║ █╗ ██║█████╗  █████╗  ██████╔╝█████╗  ██████╔╝")
	print("██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ╚════██║██║███╗██║██╔══╝  ██╔══╝  ██╔═══╝ ██╔══╝  ██╔══██╗")
	print("██║ ╚═╝ ██║██║██║ ╚████║███████╗███████║╚███╔███╔╝███████╗███████╗██║     ███████╗██║  ██║")
	print("╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝")
	print(rgb(255,255,255) + "Try to find all cases without exploding a mine. \nGood luck !")
	while (1):
		print(rgb(255,255,255) + "Choose a difficulty: 0, 1, 2")
		inp = input()
		if (not inp.isdigit()):
			print(clear + rgb(255,0,0) + "Difficulty must be a number !")
			continue
		if (inp == "0"):
			facile()
			break
		elif (inp == "1"):
			moyen()
			break
		elif (inp == "2"):
			difficile()
			break
		else:
			print(clear + rgb(255,0,0) + "This difficulty doesn't exist.")

if __name__ == "__main__":
	main()