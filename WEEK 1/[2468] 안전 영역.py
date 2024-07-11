import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
height = []
for i in range(N):
    height.append(list(int(i) for i in sys.stdin.readline().split()))

def check_now(height, check, N, rain):
    temp = 0
    for i in range(N):
        for j in range(N):
            if height[i][j] > rain and not check[i][j]:
                temp += 1
                check[i][j] = True
                checker(i,j,k)
    return temp

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def checker(x, y, rain):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not check[nx][ny] and height[nx][ny]>rain:
            check[nx][ny] = True
            checker(nx,ny,rain)

num = 1
for k in range(max([max(i) for i in height])):
    check = [[False]*N for i in range(N)]
    num = max(num, check_now(height, check, N, k))
    
print(num)