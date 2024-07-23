import sys
input= sys.stdin.readline

N, M  = (int(i) for i in input().split())

coins = [] 
for i in range(N):
    coins.append(int(input()))

result = 0

for coin in coins[::-1]:
    result += M//coin
    M -= M//coin*coin

print(result)