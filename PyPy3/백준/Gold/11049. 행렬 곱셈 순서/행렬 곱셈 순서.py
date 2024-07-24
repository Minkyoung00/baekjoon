import sys
input = sys.stdin.readline

N = int(input())
matrices = [tuple(int(i) for i in input().split()) for j in range(N)]

memo = [[0]*N for i in range(N)]

for term in range(1, N):
    for start in range(N):
        if start+term > N-1:
            break
            
        memo[start][start+term] = int(2**31)

        for i in range(start, start+term):
            memo[start][start+term] = min(memo[start][start+term], memo[start][i] + memo[i+1][start+term] + matrices[start][0]*matrices[i][1]*matrices[start+term][1])

print(memo[0][N-1])