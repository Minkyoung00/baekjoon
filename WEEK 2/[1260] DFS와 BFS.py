import sys
input = sys.stdin.readline

def BFS(graph,V):
    visited = []
    queue = [V]

    while queue:
        node = queue.pop(0) 
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))
    return visited

def DFS(graph, V):
    visited = []
    stack = [V]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(sorted(graph[node], reverse=True))
    return visited

N, M, V = (int(i) for i in input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    u, v = (int(i) for i in input().split())
    graph[u].append(v)
    graph[v].append(u) 

print(*DFS(graph, V),sep=" ")
print(*BFS(graph, V),sep=" ")
