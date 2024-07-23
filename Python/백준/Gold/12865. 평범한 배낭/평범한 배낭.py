N, K = (int(i) for i in input().split())  # N: 물품 수, K: 최대 무게
items = []
for i in range(N):
    W, V = (int(i) for i in input().split())  # W: 무게, V: 가치
    items.append((W, V))

memo = [0] * (K + 1)  

for W, V in items:
    for i in range(K, W - 1, -1):
        memo[i] = max(memo[i], memo[i - W] + V)

max_val = max(memo)

print(max_val)