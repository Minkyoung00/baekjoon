import sys
input = sys.stdin.readline

class Node:
    def __init__(self,num,parent):
        self.num = num
        self.parent = parent

def find_parent(graph):
    visited, stack = [None]*(N+1), [Node(1,None)]

    while stack:
        node = stack.pop()
        if not visited[node.num]:
            visited[node.num] = node.parent
            stack.extend(Node(i,node.num) for i in graph[node.num])

    return visited

N = int(input())

graph = [[] for i in range(N+1)]
for i in range(N-1):
    u, v = (int(j) for j in input().split())
    graph[u].append(v)
    graph[v].append(u) 

for i in find_parent(graph)[2:]:
    print(i)
