N = int(input())
couns = [[int(j) for j in input().split()] for i in range(N)]
memo = [0 for i in range(N)]


for i in range(N-1,-1,-1):
    if i == N-1:
        if couns[i][0] <= N-i:
            memo[i] = couns[i][1]
        continue

    duration = couns[i][0]

    if duration > N-i:
        memo[i] = memo[i+1]
    elif i + duration == N:
        memo[i] = couns[i][1]
    else:
        memo[i] = couns[i][1] + max(memo[i + duration:])

print(max(memo))