import sys
input = sys.stdin.readline

class Stack:
    def __init__(self, N) -> None:
        self.stk = [None]*N
        self.ptr = 0
    
    def push(self, value):
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def pop(self):
        if self.ptr <= 0:
            return -1 
        self.ptr -= 1
        return self.stk[self.ptr]

    def size(self):
        return self.ptr

    def empty(self):
        if self.ptr <= 0:
            return 1
        else:
            return 0
    
    def top(self):
        if self.ptr <= 0:
            return -1 
        return self.stk[self.ptr-1]


def order(inp,s):
    if inp == 'pop':
        print(s.pop())
    elif inp == 'size':
        print(s.size())
    elif inp == 'empty':
        print(s.empty())
    elif inp == 'top':
        print(s.top()) 
    else:
        inp = inp.split()
        X = int(inp[1])
        s.push(X)     

N = int(input())
s = Stack(N)
for i in range(N):
    order(input().strip(),s)
