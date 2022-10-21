def antisymetrique(M):
    return all(M[i][j] == -M[j][i] for i in range(len(M)) for j in range(len(M)))
