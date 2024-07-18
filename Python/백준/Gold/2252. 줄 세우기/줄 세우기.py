import sys
input = sys.stdin.readline

def topo(graph,indegree):
    result,stack = [], []

    for i in range(1, N+1):      # 진입차수가 1인 노드 Stack 추가
        if indegree[i] == 0:
            stack.append(i)

    while stack:
        u = stack.pop()
        result.append(u)
        for j in graph[u]:
            indegree[j] -= 1
            if indegree[j] == 0:
                stack.append(j)

    print(*result)  

N, M = (int(i) for i in input().split())
compare = [[] for i in range(N+1)]
indegree= [0]*(N+1)
for i in range(M):
    u, v = (int(i) for i in input().split())
    compare[u].append(v)
    indegree[v] +=1             

topo(compare,indegree)