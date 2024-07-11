T = int(input())
for i in range(T):
    n = int(input())    
    
    for j in range(n//2,1,-1):
        prime = True   
        for k in range(2,j):   
            if j%k == 0:
                prime = False  
                break
        if prime:
            j_pair = n - j
            for l in range(2,j_pair):
                if j_pair%l == 0:
                    prime = False
                    break
            if prime:
                print(j,j_pair)
                break