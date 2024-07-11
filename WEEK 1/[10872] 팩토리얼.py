def facto(n): 
    if n <= 1:
        return 1
    return facto(n-1)*n

N = int(input())
print(facto(N))
