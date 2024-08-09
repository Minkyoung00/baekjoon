A, B = int(input()), int(input())

B1, B2, B3 = B//100, B%100//10, B%10

print(A * B3)
print(A * B2)
print(A * B1)
print(A * B)