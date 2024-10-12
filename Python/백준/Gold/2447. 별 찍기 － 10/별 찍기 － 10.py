def func(N, row, col):
    if N == 3:
        result[row+1][col+1] = ' '
        return

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                for k in range(N//3):
                    for l in range(N//3):
                        result[row+N//3+k][col+N//3+l] = ' '
            else:
                func(N//3, row + N//3*i, col + N//3*j)

N = int(input())
result = [['*']*N for i in range(N)]

func(N, 0, 0)

for i in result:
    print("".join(i))