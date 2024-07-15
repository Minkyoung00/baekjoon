import sys

def make_graph(arr, i,graph): # i : 탐색할 노드 index
    if i >= len(arr):
        return
    
    u = arr[i]
    left, right = '.','.'

    if i+1 < len(arr) and u > arr[i+1]:
        left = arr[i+1]
    
    j = i+1
    while j < len(arr) and u > arr[j]:
        j += 1
       
    if j < len(arr):
        if i == 0 or arr[i-1] > arr[j] or arr[j] != max(arr[:i+1]):
            right = arr[j]

            for n in range(len(graph)):
                if right == graph[n][2]:
                    right = '.'  

    graph.append([u,left,right])
    make_graph(arr, i+1,graph)

def postorder(arr, v):  
    if v == '.':
        return
    
    for n in graph:
        if v == n[0]:  
            postorder(arr, n[1])   
            postorder(arr, n[2]) 
            print(v)  
            return

sys.setrecursionlimit(10**8)
lines = sys.stdin.readlines()
pre = [int(line.strip()) for line in lines]

graph = []
make_graph(pre, 0, graph)
postorder(graph, pre[0])