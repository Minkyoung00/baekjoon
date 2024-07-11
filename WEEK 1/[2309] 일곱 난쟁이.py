height = []
for i in range(9):
    height.append(int(input())) 

for i in height:
    one_not = sum(height)-100-i
    if one_not in height and one_not != i:
        height.remove(i)
        height.remove(one_not)
        break
    
for i in sorted(height):
    print(i)