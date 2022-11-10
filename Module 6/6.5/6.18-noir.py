def possible_values(grid, row, col):
    """Return the possible values for a cell."""
    possible = [i for i in range(1, 10)]
    for i in range(9):
        if grid[row][i] in possible:
            possible.remove(grid[row][i])
        if grid[i][col] in possible:
            possible.remove(grid[i][col])
    for i in range(3):
        for j in range(3):
            if grid[row//3*3+i][col//3*3+j] in possible:
                possible.remove(grid[row//3*3+i][col//3*3+j])
    return possible

def check_rows(board):
    for row in board:
        checker = [i for i in range(1, 10)]
        for i in row:
            if i in checker:
                checker.remove(i)
            else:
                return False
    return True

def check_cols(board):
    for i in range(9):
        checker = [i for i in range(1, 10)]
        for row in board:
            if row[i] in checker:
                checker.remove(row[i])
            else:
                return False
    return True

def check_regions(board):
    for i in range(3):
        for j in range(3):
            checker = [i for i in range(1, 10)]
            for row in board[i*3:(i+1)*3]:
                for col in row[j*3:(j+1)*3]:
                    if col in checker:
                        checker.remove(col)
                    else:
                        return False
    return True

def check_sudoku(board):
    return check_rows(board) and check_cols(board) and check_regions(board)

def naked_single(grid):
    """Find the naked single in the grid and fill the grid."""
    found = False
    if check_sudoku(grid):
        print("Status : Solved.")
        return True, grid
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                possible = possible_values(grid, row, col)
                if len(possible) == 1:
                    grid[row][col] = possible[0]
                    print(f"Status : Naked single found, new value at ({row}, {col}) : {grid[row][col]}")
                    found = True
    return naked_single(grid) if found else (found, None)