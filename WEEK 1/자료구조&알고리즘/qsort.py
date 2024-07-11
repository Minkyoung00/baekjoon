def qsort(a, left, right):
    pl = left
    pr = right
    x = a[(left+right)//2]

    while pl <= pr:
        while a[pl] < x: pl += 1    #pl이 피벗보다 큰 수를 가리킬 때까지 pl 오른쪽 이동
        while a[pr] > x: pr -= 1    #pr이 피벗보다 작은 수를 가리킬 떄까지 pr 왼쪽으로 이동
        if pl <= pr:        
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

num = 9
x = [5,8,4,2,6,1,3,9,7]

qsort(x, 0, num-1 )
print(x)


