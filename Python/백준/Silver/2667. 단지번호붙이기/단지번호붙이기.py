import sys
input = sys.stdin.readline

def bfs(graph, N):
    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)
    visited = [[False]*N for i in range(N)]
    all_num, result = 0, []

    for i in range(N):  # i: 행
        for j in range(N):  # j: 열
            if graph[i][j] == '1' and not visited[i][j] : # (집이 있는 경우) AND (아직 방문 안 한 경우)만 보기 위해
                queue = [(i,j)]
                visited[i][j] = True
                temp = 1
        
                while queue:
                    y, x = queue.pop(0)
                    for k in range(4):
                        new_x = x + dx[k]
                        new_y = y + dy[k]
                        if 0 <= new_x < N and 0 <= new_y < N and info[new_y][new_x] == '1' and not visited[new_y][new_x]:
                            queue.append((new_y,new_x))
                            visited[new_y][new_x] = True
                            temp += 1

                result.append(temp)
                all_num += 1
    result.sort()
    print(all_num) 
    print(*result, sep="\n")

N = int(input())
info = []
for i in range(N):
    info.append(input().strip())

bfs(info,N)