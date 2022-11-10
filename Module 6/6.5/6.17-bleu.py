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