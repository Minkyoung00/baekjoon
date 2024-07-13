def preorder(arr, v):        
    if v == '.':
        return
    u = v 

    print(u,end ="")
    for n in range(N):
        if u == arr[n][0]: 
            preorder(arr, arr[n][1])
            preorder(arr, arr[n][2])
            break

def inorder(arr, v):        
    if v == '.':
        return 
    u = v 
    
    for n in range(N):
        if u == arr[n][0]:  
            inorder(arr, arr[n][1])
            print(u,end ="")
            inorder(arr, arr[n][2])
            break

def postorder(arr, v):  
    if v == '.':
        return
    u = v
    for n in range(N):
        if u == arr[n][0]:  
            postorder(arr, arr[n][1])   
            postorder(arr, arr[n][2]) 
            print(u,end ="")  
    return

N = int(input())
graph = []                             
for i in range(N):                            
    graph.append(input().split())

preorder(graph, 'A')
print()
inorder(graph, 'A')
print()
postorder(graph, 'A')
print()