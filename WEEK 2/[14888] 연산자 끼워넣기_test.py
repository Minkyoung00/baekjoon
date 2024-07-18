def dfs(u, visited = []):
    global graph
    visited.append(u)
    for v in graph[u]:
        if v not in visited:
            visited = dfs(v,visited)
    
    return visited

N = int(input())    # 수의 개수
A = [int(i) for i in input().split()]  # 수 배열
hap, cha, gop, na  = [int(i) for i in input().split()]
oper_list = ['+']*hap + ['-']*cha + ["*"]*gop + ["//"]*na
