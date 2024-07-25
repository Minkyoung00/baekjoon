N = int(input())
V = [int(input()) for _ in range(N)]

memo = [0] * N

if N > 0:
    memo[0] = V[0]
if N > 1:
    memo[1] = V[0] + V[1]
if N > 2:
    memo[2] = max(V[0] + V[2], V[1] + V[2])

for i in range(3, N):
    memo[i] = max(memo[i-2], memo[i-3] + V[i-1]) + V[i]

print(memo[N-1])