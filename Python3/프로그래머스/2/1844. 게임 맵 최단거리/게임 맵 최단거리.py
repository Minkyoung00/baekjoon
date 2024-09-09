from collections import deque

def solution(maps):
    m, n = len(maps[0]), len(maps)  # m: 열, n: 행
    visited = [[False] * m for _ in range(n)]  # n행 m열
    visited[0][0] = True

    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)

    queue = deque([(0, 0, 1)])  # dist는 1부터 시작 (첫 칸도 포함)

    while queue:
        x, y, dist = queue.popleft()  # pop(0) 대신 deque의 popleft() 사용

        for k in range(4):
            n_x = x + dx[k]
            n_y = y + dy[k]
            if 0 <= n_x < m and 0 <= n_y < n and maps[n_y][n_x] == 1 and not visited[n_y][n_x]:
                queue.append((n_x, n_y, dist + 1))
                visited[n_y][n_x] = True

                if n_x == m - 1 and n_y == n - 1:
                    return dist + 1

    return -1