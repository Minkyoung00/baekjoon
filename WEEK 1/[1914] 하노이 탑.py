def hanoi(n,s,e,m):
    if n == 1:
        print(s,e)
        return 
    hanoi(n-1,s,m,e)
    hanoi(1,s,e,m)
    hanoi(n-1,m,e,s)
    
N = int(input())
print(2**N-1)
if N <= 20:
    result = hanoi(N,1,3,2)