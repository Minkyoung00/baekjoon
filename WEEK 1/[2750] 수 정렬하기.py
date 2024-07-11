N = int(input())
temp1 = [None]*(1000+1)    #양수
temp2 = [None]*(1000+1)    #음수

for i in range(N):
    a = int(input())
    if a == abs(a):
        temp1[a] = str(a)
    else:
        temp2[-a] = a

temp2.reverse()
temp = temp2 + temp1

for i in temp:
    if i:
        print(i)