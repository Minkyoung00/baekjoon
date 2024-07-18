import sys
input = sys.stdin.readline

def path(graph):
    result = 0
    for i in range(1, N+1):
        if A[i] == '1':
            visited = []
            stack = [i]
            while stack:
                u = stack.pop()
                visited.append(u)
                for v in graph[u]:
                    if v not in visited:
                        if A[v] == '1':
                            result += 1
                        else:
                            stack.append(v)
    return result

N = int(input())    # 정점 수
A = "X" + input()         # 실내외 "문자열"

graph = [[] for _ in range(N+1)]    # 인접 리스트
for i in range(N-1):                        
    u, v = (int(i) for i in input().split())    # u,v : 간선 열결 정보
    graph[u].append(v)
    graph[v].append(u)

print(path(graph))

