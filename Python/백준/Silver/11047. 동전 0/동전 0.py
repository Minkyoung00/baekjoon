import sys
input= sys.stdin.readline

N, M  = (int(i) for i in input().split())

coins = [] 
for i in range(N):
    coins.append(int(input()))

result = 0
coins.reverse()

for coin in coins:
    if coin <= M:
        max_in = M//coin
        result += max_in
        M = M - max_in*coin
print(result)