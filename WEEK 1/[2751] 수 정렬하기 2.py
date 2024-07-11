import sys
N = int(sys.stdin.readline())
temp = [None]*2000001

for i in range(N):
    a = int(sys.stdin.readline())
    temp[1000000+a] = str(a) 

for i in temp:
    if i:
        print(i)