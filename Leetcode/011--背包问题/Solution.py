def bag(n, c, w, v):
    f = [[0 for j in range(c+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, c+1):
            f[i][j] = f[i-1][j]
            if j > w[i-1] and f[i][j] < f[i-1][j - w[i-1] + v[i-1]]:
                f[i][j] = f[i-1][j - w[i-1] + v[i-1]]
    return f
