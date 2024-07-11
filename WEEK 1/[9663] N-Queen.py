num = 0

def set(i):  
    global num
    global N  
    for j in range(N):
        if not line[j] and not crossUp[j+i] and not crossDown[(N-1)-i+j]:
            pos[i] = j 
            if i == N-1:
                num += 1
            else:
                line[j] = crossUp[j+i] = crossDown[(N-1)-i+j] = True
                set(i+1)
                line[j] = crossUp[j+i] = crossDown[(N-1)-i+j] = False
            
N = int(input())
pos = [0]*N
line = [False]*N
crossUp = [False]*(2*N-1)
crossDown = [False]*(2*N-1)
set(0)
print(num)