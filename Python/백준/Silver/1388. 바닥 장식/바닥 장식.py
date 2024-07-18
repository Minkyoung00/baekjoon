import sys
input = sys.stdin.readline

N,M = (int(i) for i in input().split()) # N: 세로, M: 가로
deco_list = []
for i in range(N):
    deco_list.append(input().strip())

def deco_num(deco_list):
    result = 0
    for i in range(N):
        for j in range(M):
            current = deco_list[i][j]
            to_look = []
            if i != 0:
                up = deco_list[i-1][j]
                if up == "|":
                    to_look.append(up)
            if j != 0:
                left = deco_list[i][j-1]
                if left == "-":
                    to_look.append(left)
            if current not in to_look:
                result += 1
    return result

print(deco_num(deco_list))