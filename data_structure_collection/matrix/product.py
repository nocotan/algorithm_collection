

def product(m1, m2, mat1, n1, n2, mat2):
    res = [[0 for x in range(n2)] for y in range(m1)]

    for i in range(m1):
        for j in range(n2):
            res[i][j] = 0
            for x in range(m2):
                res[i][j] += mat1[i][x] * mat2[x][j]

    return res
