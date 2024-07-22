import sys
input = sys.stdin.readline

n = int(input())

table = [0,1,2] + [0]*(n-2)
for i in range(3,n+1):
    table[i]= (table[i-1] + table[i-2]) % 15746

print(table[n])