# 곱셈에 대한 모듈로 성질
# (a*b) mod m = [(a mod m)*(b mod m)] mod m

A, B, C = input().split()
A, B, C = int(A), int(B), int(C)

def exponen(A,B,C):
    if B == 0:
        return 1
    temp = exponen(A,B//2,C)
    temp = temp*temp % C
    if B%2 != 0:
        temp = (temp*A)%C
    return temp
    
print(exponen(A,B,C))