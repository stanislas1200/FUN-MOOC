import sys
import os
from getkey import getkey

# define colors
clear = "\x1b[H\x1b[2J"
bold_c = "\x1b[0m\x1b[1m"


def rgb(r, g, b): return f"\u001b[38;2;{r};{g};{b}m"

def error(type, message):
	print(f"{bold_c}{rgb(228,0,0)}Error{bold_c}: {rgb(255,215,0)}{type}{bold_c}: {message}")

def import_card(path):
	if (not os.path.isfile(path)):
		error("File", f"File does not exist: [{rgb(75,0,130)}{path}{bold_c}]")
		return exit(1)
	with open(path, "r") as f:
		lines = f.readlines()
	board_size = tuple(map(int, lines[0].split(',')))
	tetrominos = []

	for line in lines[1:]:
		line_data = line.strip().split(';')
		line_data = list(filter(None, line_data))
		coordinates = [tuple(map(int, pair.strip('()').split(','))) for pair in line_data[:-3]]
		color = ';'.join(line_data[-3:])
		tetrominos.append([coordinates, color, (0,0)])

	result = (board_size, tetrominos)
	return result

def create_grid(x, y):
	x = x * 3 + 2
	y = y * 3 + 2
	grid = []
	for i in range(y):
		grid.append([])
		for j in range(x):
			if (j == x // 3) and i > y // 3 and i < y // 3 * 2 - 1 + 2:
				grid[i].append(' |')
			elif (j == x // 3 * 2 - 1 + 2) and i > y // 3 and i < y // 3 * 2 - 1 + 2:
				grid[i].append('| ')
			elif (i == y // 3 or i == y // 3 * 2 - 1 + 2) and j > x // 3 and j < x // 3 * 2 - 1 + 2:
				grid[i].append('--')
			else:
				grid[i].append('  ')
	return grid

def setup_tetraminos(tetramino, initial_grid):
	grid = [row[:] for row in initial_grid]
	board_width = len(grid[0]) // 3 + 1
	board_height = len(grid) // 3 + 1
	nb = 0
	x = 0
	y = 0
	skip = 0
	for obj in tetramino:
		nb += 1
		if (nb == 5):
			skip = 1
		x = (nb + skip - 1) % 3
		y = (nb + skip - 1) // 3

		offset = (x * board_width, y * board_height)
		obj[2] = offset
		for coord in obj[0]:
			try:
				grid[coord[1] + offset[1]][coord[0] + offset[0]] = f'\x1b[{obj[1]}m{nb} \x1b[0m'
			except IndexError:
				error("Tetramino", f"Tetramino {nb} is out of bounds")
				exit(1)
			
	return grid, tetramino

def print_title(grid):
	title_len = len("  _______ __ _                       _                 ")
	title_padding = 0
	padding = 0
	if len(grid[0]) * 2 < title_len:
		padding = (title_len - len(grid[0])) // 3
	else:
		title_padding = len(grid[0]) - title_len // 2
	print(rgb(228, 143, 69))
	print(f"{title_padding * ' '}  _______ __ _                       _                 ")
	print(f"{title_padding * ' '} |__   __/_/| |                     (_)                ")
	print(f"{title_padding * ' '}    | |  ___| |_ _ __ __ _ _ __ ___  _ _ __   ___  ___ ")
	print(f"{title_padding * ' '}    | | / _ \ __| '__/ _` | '_ ` _ \| | '_ \ / _ \/ __|")
	print(f"{title_padding * ' '}    | ||  __/ |_| | | (_| | | | | | | | | | | (_) \__ \\")
	print(f"{title_padding * ' '}    |_| \___|\__|_|  \__,_|_| |_| |_|_|_| |_|\___/|___/")
	return padding

def print_grid(grid, no_number=True):
	padding = print_title(grid)
	print(bold_c, rgb(107,36,12),f"{padding * ' '}╔", "══" * (len(grid[0])), "╗", sep='')
	for line in grid:
		print(bold_c, rgb(107,36,12), f"{padding * ' '}║", sep='', end='')
		for cell in line:
			color_start = cell.find('\x1b[')
			color_end = cell.find('m') + 1
			if no_number and cell[color_start:color_end]:
				print(f'{cell[color_start:color_end]}  ', end='\x1b[0m')
			else:
				print(cell, end='')
		print(bold_c, rgb(107,36,12), "║", sep='')
	print(bold_c, rgb(107,36,12), f"{padding * ' '}╚", "══" * (len(grid[0])), "╝", sep='')
	print("\x1b[0m")

def check_win(grid):
	w = len(grid[0])
	h = len(grid)
	for y in range(h):
		for x in range(w):
			if not (x > w // 3 and x < w // 3 * 2 - 1 + 2 and y > h // 3 and y < h // 3 * 2 - 1 + 2):
				if (grid[y][x] != '  ' and grid[y][x] != ' |' and grid[y][x] != '| ' and grid[y][x] != '--'):
					return False
	return True

def move_tetramino(grid, tetraminos, tetramino, board):
	invalid = False
	while True:
		print(clear)
		updated_board = [row[:] for row in board]
		print_grid(animate_fish(place_tetraminos(tetraminos, updated_board)), True)
		print(f"{bold_c}{rgb(228, 143, 69)}Move the tetramino:{bold_c}")
		print(f"{bold_c}{rgb(228, 143, 69)}[ikjl] to move up down left right, [o/u] to rotate, [v] to validate{bold_c}")
		print(f"{bold_c}{rgb(228, 143, 69)}[ESC] to exit{bold_c}")
		if (invalid):
			error("Move", "Invalid move")
			invalid = False
		b, keyname = getkey()
		if (keyname == 'i' and tetramino[2][1] > 0):
			tetramino[2] = (tetramino[2][0], tetramino[2][1] - 1)
		elif (keyname == 'k' and tetramino[2][1] < len(grid) - 1):
			tetramino[2] = (tetramino[2][0], tetramino[2][1] + 1)
		elif (keyname == 'j' and tetramino[2][0] > 0):
			tetramino[2] = (tetramino[2][0] - 1, tetramino[2][1])
		elif (keyname == 'l' and tetramino[2][0] < len(grid[0]) - 1):
			tetramino[2] = (tetramino[2][0] + 1, tetramino[2][1])
		elif (keyname == 'o'):
			tetramino[0] = rotate_tetramino(tetramino)[0]
		elif (keyname == 'u'):
			tetramino[0] = rotate_tetramino(tetramino, False)[0]
		elif (keyname == 'v'):
			if (check_move(tetramino, grid) and not is_overlaping(tetramino, tetraminos)):
				return place_tetraminos(tetraminos, updated_board)
			else:
				invalid = True
		elif (keyname == 'esc'):
			raise KeyboardInterrupt
		else:
			continue

def select_tetramino(grid, tetraminos, board):
	keyname = ''
	invalidInput = False
	while True:
		print(clear)
		animate_fish(grid)
		print_grid(grid, False)
		if (invalidInput):
			error("Input", f"Invalid input: [{rgb(75,0,130)}{keyname}{bold_c}]")
		print(f"{bold_c}{rgb(228, 143, 69)}Select a tetramino:{bold_c}")
		print(f"{bold_c}{rgb(228, 143, 69)}[ESC] to exit{bold_c}")
		b, keyname = getkey()
		if (keyname == 'esc'):
			raise KeyboardInterrupt
		elif (keyname < '1' or keyname > str(len(tetraminos))):
			invalidInput = True
			continue
		return move_tetramino(grid, tetraminos, tetraminos[int(keyname) - 1], board)
	
def place_tetraminos(tetraminos, grid):
	nb = 0
	for tetramino in tetraminos:
		nb += 1
		coordinates = tetramino[0]
		color = tetramino[1]
		offset = tetramino[2]

		for coord in coordinates:
			x, y = coord
			x += offset[0]
			y += offset[1]

			if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
				if grid[y][x].find('XX') != -1:
					grid[y][x] = f'\x1b[{color}mXX\x1b[0m'
				else:
					grid[y][x] = f'\x1b[{color}m{nb} \x1b[0m'

	return grid

def is_overlaping(tetramino, tetraminos):
	coordinates = tetramino[0]
	offset = tetramino[2]
	for coord in coordinates:
		x, y = coord
		x += offset[0]
		y += offset[1]
		for obj in tetraminos:
			if obj != tetramino:
				for coord2 in obj[0]:
					x2, y2 = coord2
					x2 += obj[2][0]
					y2 += obj[2][1]
					if x == x2 and y == y2:
						return True
	return False

def check_move(tetramino, grid):
	coordinates = tetramino[0]
	offset = tetramino[2]
	for coord in coordinates:
		x, y = coord
		x += offset[0]
		y += offset[1]
		if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
			if grid[y][x].find('XX') != -1 or grid[y][x].find('--') != -1 or grid[y][x].find(' |') != -1 or grid[y][x].find('| ') != -1:
				return False
		else:
			return False
	return True

def rotate_tetramino(tetramino, clockwise=True):
	coordinates, color, offset = tetramino
	if (clockwise):
		rotated_coordinates = [(-y, x) for x, y in coordinates]
	else:
		rotated_coordinates = [(y, -x) for x, y in coordinates]
	rotated_tetramino = [rotated_coordinates, color, offset]
	return rotated_tetramino

fish_poss = (0,0)
fish_dir = 1

def animate_fish(grid):
	global fish_poss
	global fish_dir
	fish = ">0" if fish_dir == 1 else "0<"
	fish = f"{rgb(0, 0, 255)}{fish}{bold_c}"
	x, y = fish_poss
	grid[y][x] = '  '
	if (fish_dir == 1):
		if (x + 1 >= len(grid[0]) or grid[y][x + 1] != '  '):
			fish_dir = -1
		else:
			x += 1
	else:
		if (x - 1 < 0 or grid[y][x - 1] != '  '):
			fish_dir = 1
		else:
			x -= 1
	fish_poss = (x, y)
	grid[y][x] = fish
	return grid

def win(grid):
	print(clear)
	print_grid(grid, False)
	print(f"{bold_c}{rgb(228, 143, 69)} ^ ^")              
	print(f"{bold_c}{rgb(228, 143, 69)}(O,O)")             
	print(f"{bold_c}{rgb(228, 143, 69)}(   ) congrats" )   
	print(f'{bold_c}{rgb(228, 143, 69)}-"-"--------------')
	print("\x1b[0m")

def main():
	if (len(sys.argv) != 2):
		return error("Usage", f"python3 tetramino.py [{rgb(75,0,130)}file{bold_c}]")
	print(clear)
	data = import_card(sys.argv[1])
	board = create_grid(data[0][0], data[0][1])
	grid, tetraminos = setup_tetraminos(data[1], board)
	try:
		while True:
			grid = select_tetramino(grid, tetraminos, board)
			grid[fish_poss[1]][fish_poss[0]] = '  '
			if (check_win(grid)):
				win(grid)
				break
	except (KeyboardInterrupt, SystemExit):
		pass
	return

if __name__ == '__main__':
	main()
