def trace(M):
    return sum(M[i][i] for i in range(len(M)))
