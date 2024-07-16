import sys
input = sys.stdin.readline

def Connected(graph):
    visited = []
    result = 0
    for i in range(1,N+1):
        if i not in visited:
            stack = [i]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.append(node)
                    stack.extend(graph[node])
            result += 1
    return result

N, M = (int(i) for i in input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    u, v = (int(j) for j in input().split())
    graph[u].append(v)
    graph[v].append(u) 

print(Connected(graph))