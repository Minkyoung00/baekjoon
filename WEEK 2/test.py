def preorder(arr, i):        
    #
    need_visit_stack = [None]*N
    top = 0
    visited = []
    #
    need_visit_stack[top] = 0   #stack.push
    top += 1

    while top > 0:
        top -= 1
        u = need_visit_stack[top]   #stack.pop

        if u not in visited:             # 아직 방문 안 했다면
            visited.append(u)
            for v in reversed(graph[u]): # 전위순회임(왼쪽을 먼저 봐야됨)과 stack의 특성을 고려해(늦게 들어온 게 일찍 나옴) reverse
                if v > 0:        
                    need_visit_stack[top] = v
                    top += 1

    return visited

def inorder(arr, i):        
    #
    need_visit1 = [None]*N  # 곧 방문 stack
    need_visit2 = [None]*N  # 나중 방문할 Stack
    top1 = 0
    top2 = 0
    visited = []

    need_visit1[top1] = u = 0   #stack.push
    top1 += 1

    while graph[u][0] or graph[u][1]:
        top1 -= 1
        u = need_visit1[top1]

        if graph[u][0] > 0:      #왼쪽  
            need_visit1[top1] = graph[u][0]
            top1 += 1

        if graph[u][1]> 0:     #오른쪽                
            need_visit2[top2] = graph[u][1]
            top2 += 1
    
    while True:
        u = need_visit1[top1]
        visited.append(u)
        top1 -= 1
                                                                                                                                           
        
    return visited

def postorder(arr, i):        
    #
    need_visit_stack = [None]*N
    top = 0
    visited = []
    #
    need_visit_stack[top] = 0   #stack.push
    top += 1

    while top > 0:
        top -= 1
        u = need_visit_stack[top]   #stack.pop

        if u not in visited:             # 아직 방문 안 했다면
            visited.append(u)
            for v in reversed(graph[u]): # 전위순회임(왼쪽을 먼저 봐야됨)과 stack의 특성을 고려해(늦게 들어온 게 일찍 나옴) reverse
                if v > 0:        
                    need_visit_stack[top] = v
                    top += 1

    return visited

# 노드 개수 N
N = int(input())
graph = []                                    # 입력 N번 받아서 각 노드 별 연결 노드를 나타내는 인접 리스트 생성
for i in range(N):                                  # 아스키 코드로 알파벳 -> 숫자 변환
    graph.append(input().split())
    # inp = [ord(j)-65 for j in input().split()]      # index와 노드 이름 일치 시키기
    # graph[inp[0]] = inp[1:] 
print(graph)
#graph = [[1, 2], [3, -19], [4, 5], [-19, -19], [-19, -19], [-19, 6], [-19, -19]]

result1 = ""
for i in preorder (graph, 0):
    result1 += str(chr(i+65))
print(result1)

result2 = ""
for i in inorder(graph, 0):
    result2 += str(chr(i+65))
print(result2)

result3 = ""
for i in postorder(graph, 0):
    result3 += str(chr(i+65))
print(result3)

