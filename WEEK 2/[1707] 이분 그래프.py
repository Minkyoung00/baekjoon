import sys
input = sys.stdin.readline

def is_bipartite(graph):
    check = [-1 for _ in range(V+1)]

    for i in range(1,V+1):      # 비연결 그래프 고려
        if check[i] == -1:      # 노드 i가 탐색 전이면
            stack = [i]         # 노드 i를 시작 노드로
            check[i] = 0        # 시작 노드 색 처리
            while stack:        
                u = stack.pop()     # u: stack 추출
                for v in graph[u]:  # v: u 인접 노드
                    if check[v] == -1:          ### v가 탐색 전이면
                        check[v] = 1- check[u]  # u와 다른 색 부여
                        stack.append(v)         # stack에 넣기
                    elif check[v] == check[u]:  ### u와 v가 같은 색
                        return "NO"             # 이분그래프 아님 
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