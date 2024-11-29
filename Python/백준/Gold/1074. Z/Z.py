N, r ,c = (int(i) for i in input().split())

result = 0

while N:
    if r < 2**(N-1) and c < 2**(N-1):
        pass
    elif r < 2**(N-1) and c >= 2**(N-1):
        result += 4**(N-1)
        c -= 2**(N-1)
    elif r >= 2**(N-1) and c < 2**(N-1):
        result += 2*4**(N-1)
        r -= 2**(N-1)
    else:
        result += 3*4**(N-1)
        c -= 2**(N-1)
        r -= 2**(N-1)
    N -= 1

print(result)