N = int(input())
num = 0

a = input().split()

for i in a:
    i = int(i)
    
    temp = 0
    for j in range(2,i):
        if i%j == 0:
            temp += 1
            
    if temp == 0:
        if i !=1:
            num += 1