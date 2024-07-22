import sys
input = sys.stdin.readline

n = int(input())

if n < 3:
    print(n)
else:
    n_2, n_1 = 1, 2
    result = 1
    for i in range(n-2):
        result = (n_1 + n_2) % 15746
        n_2 = n_1
        n_1 = result

    print(result)