n = int(input())

if n < 3:
    print(1)
else:
    n_2, n_1 = 1, 1
    result = 0

    for i in range(n-2):
        result = n_1 + n_2
        n_2 = n_1
        n_1 = result

    print(result)