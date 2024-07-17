import sys
input = sys.stdin.readline

def is_bipartite(graph):
    check = [-1 for _ in range(V+1)]

    for i in range(1,V+1):
        if check[i] == -1:
            stack = [i]
            check[i] = 0
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if check[v] == -1:
                        check[v] = 1- check[u]
                        stack.append(v)   
                    elif check[v] == check[u]:
                        return "NO"
    return "YES"                   

K = int(input())


for i in range(K):
    V, E = (int(j) for j in input().split())

    graph = [[] for i in range(V+1)]    
    for k in range(E):
        u, v  = (int(j) for j in input().split())
        graph[u].append(v)
        graph[v].append(u)

    print(is_bipartite(graph))