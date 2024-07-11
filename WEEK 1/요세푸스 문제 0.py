def yoseipus(arr):
    third = K-1
    new = []

    while True:
        new.append(arr[third])
        del arr[third]

        if len(arr) == 0:
            return new
        third = (third +K-1) % len(arr)




N, K = (int(i) for i in input().split())    
people = [ i for i in range(1, N + 1)]  
print("<", end="")
print(*yoseipus(people), sep=", ", end="")
print(">")
        
       
