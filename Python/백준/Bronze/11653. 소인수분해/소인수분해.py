N = int(input())
result = []

for i in range(2, N+1):
    while N % i == 0:
        print(i)
        N /= i
    if N == 1:
        break