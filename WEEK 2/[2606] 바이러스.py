import sys
input = sys.stdin.readline

def de_virus(graph):
    visited = []
    stack = [1]
    while stack:
        u = stack.pop()
        if u not in visited:
            visited.append(u)
            stack.extend(graph[u])

    return len(visited)-1

N = int(input())
M = int(input())

graph = [[] for i in range(N+1)]

for i in range(M):
    u, v = (int(j) for j in input().split())
    graph[u].append(v)
    graph[v].append(u) 
    
print(de_virus(graph))