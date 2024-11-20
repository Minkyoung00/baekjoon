import sys
input = sys.stdin.readline

N_A, N_B = (int(i) for i in input().split())
inter = 0

A = set(map(int, input().split()))
B = set(map(int, input().split()))

inter = len(A & B)

print(N_A + N_B - 2*inter)