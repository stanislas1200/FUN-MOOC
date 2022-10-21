def print_mat(mat):
    if not mat:
        print()
    for row in mat:
        for col in row:
            print(col, end=' ')
        print()


ma_matrice = eval(input())
print_mat(ma_matrice)
