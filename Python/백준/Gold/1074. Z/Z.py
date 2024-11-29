N, r ,c = (int(i) for i in input().split())

result = 0

def z_func():
    global result, r, c
    
    if N == 1:
        if not r and not c:
            pass
        elif not r and c:
            result += 1
        elif r and not c:
            result += 2
        else:
            result += 3 
    else:         
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

while N:
    z_func()
    N -= 1

print(result)