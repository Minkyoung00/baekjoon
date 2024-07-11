N,A,M = input(), sorted(list(input().split())), input() 

def bin_search(a, key):
    pl = 0
    pr = len(a)-1
    while True:
        pc = (pl + pr)//2
        if a[pc] == key:
            print(1)
            return
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr =pc - 1
        if pl > pr:
            print(0)
            break
    
for i in list(input().split()):
    bin_search(A,i)