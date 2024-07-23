A = input()
B = input()
len_A = len(A)
len_B = len(B)

LCS_pre = [0] * (len_A+1)
LCS_cur = [0] * (len_A+1)
max_len = 0

for i in range(len_B):
    for j in range(len_A):
        if A[j] == B[i]:
            LCS_cur[j] = LCS_pre[j-1]+1
            if LCS_cur[j] > max_len:
                max_len = LCS_cur[j]
        else:
            LCS_cur[j] = max(LCS_cur[j-1],LCS_pre[j])
    LCS_pre, LCS_cur = LCS_cur,LCS_pre

print(max_len)