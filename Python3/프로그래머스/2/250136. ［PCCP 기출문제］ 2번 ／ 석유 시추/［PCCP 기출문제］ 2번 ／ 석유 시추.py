def solution(land):
    n = len(land)       #세로
    m = len(land[0])    #가로

    trans_land = list(zip(*land))
    
    moving = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[-1] * m for i in range(n)]

    answer = 0
    fuel = []

    for j in range(m):
        if not trans_land[j]:
            continue
        count = 0

        temp = []
        for i in range(n):
            if visited[i][j] >= 0 and (visited[i][j] not in temp):
                count += fuel[visited[i][j]]
                temp.append(visited[i][j])
            if visited[i][j] < 0 and land[i][j]:
                queue = [(i,j)]
                visited[i][j] = len(fuel)

                # 석유 덩어리 만들기
                size = 0
                while queue:
                    cur_y, cur_x = queue.pop()
                    size += 1
                    for x, y in moving:
                        mov_y, mov_x = cur_y+y, cur_x+x
                        if 0 <= mov_x < m and 0 <= mov_y < n and land[mov_y][mov_x] and visited[mov_y][mov_x] < 0:
                            visited[mov_y][mov_x] = len(fuel)
                            queue.append((mov_y,mov_x))

                temp.append(len(fuel))
                fuel.append(size)
                count+=size

        answer = max(answer, count)

    return answer