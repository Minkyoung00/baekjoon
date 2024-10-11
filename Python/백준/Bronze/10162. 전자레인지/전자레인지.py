N = int(input())
result = []
cnt_min = 1001

A = N // 300

for i in range(A+1):
    temp = []
    N -= 300*i
    B = N // 60
    temp.append(i)

    for j in range(B+1):
        temp1 = temp[:]
        N -= 60*j
        C = N // 10
        temp1.append(j)

        if N % 10 == 0:
            temp1.append(C)
            if sum(temp1) < cnt_min:
                result = temp1 
if result:     
    print(*result)
else:
    print(-1)