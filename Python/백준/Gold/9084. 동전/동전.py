import sys
input= sys.stdin.readline

T = int(input())
for i in range(T):
    N  = int(input())
    coins = [int(j) for j in input().split()]   # coins = [0, 1, 2, ... , N-1]
    M = int(input()) 
    
    dp =[1] + [0]*M

    for coin in coins:
        for i in range(1,M+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[M])