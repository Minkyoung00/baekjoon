N, K = ( int(i) for i in input().split())   # N:  물품 수, K: 최대 무게 

items = []
for i in range(N): 
    W, V = ( int(i) for i in input().split())   # W: 무게, V: 가치
    items.append((W,V)) 
items.sort()

memo = [0]*(K+1)

for W,V in items:
    new = memo[:]    
    for i in range(K+1):
        if i + W > K: #
            break      
        if memo[i] != 0 or i == 0:
            new[i+W] = max( memo[i+W], memo[i] + V)   
    memo = new

print(max(memo))