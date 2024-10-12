N = int(input())
result = []

for i in [300, 60]:
    if N > 0:
        result.append(N//i)
        N %= i
    else:
        result.append(0)

if N % 10:
    print(-1)
else:
    result.append(N//10)
    print(*result)