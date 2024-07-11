import sys
def set(i):
    global wage, current_cost
    
    if i == N:
        if W[order[-1]][order[0]]:
            current_cost += W[order[-1]][order[0]]
            wage = min(wage, current_cost)
            current_cost -= W[order[-1]][order[0]]
    
    for j in range(N):
        if not check[j]:
            if i > 0 and W[order[i-1]][j] == 0:
                continue
            
            order[i] = j
            check[j] = True
            
            if i > 0:
                current_cost += W[order[i-1]][j]
            
            if current_cost < wage:
                set(i + 1)
            
            if i > 0:
                current_cost -= W[order[i-1]][j]
            
            check[j] = False

N = int(sys.stdin.readline())
W = [[]]*N

for i in range(N):
    W[i] = list(int(i) for i in sys.stdin.readline().split())

wage, current_cost = 1000000*N, 0
order = [0] * N
check = [False] * N

set(0)
print(wage)