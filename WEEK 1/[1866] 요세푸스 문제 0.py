def yoseipus(arr,del_idx):
    del_ord = del_idx-1
    new = []
    while True:
        new.append(arr[del_ord])
        del arr[del_ord]

        if len(arr) == 0:
            return new
        del_ord = (del_ord +K-1) % len(arr)

N, K = (int(i) for i in input().split())    # 7 3
people = [ i for i in range(1, N + 1)]  #[1,2,3,4,5,6,7]
print("<", end="")
print(*yoseipus(people,K), sep=", ", end="")
print(">")