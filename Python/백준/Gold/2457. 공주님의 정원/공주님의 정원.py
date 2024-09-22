N = int(input())

flowers = []
for i in range(N):
    flowers.append([int(j) for j in input().split()])

flowers = sorted(flowers, key = lambda x : (x[0], x[1], x[2], x[3]))

# 지는 월, 일 저장
temp_m, temp_d = 3, 1
cnt = i =0
end_m, end_d = 3, 1

while(i < N):
    s_m, s_d, e_m, e_d = flowers[i]
    
    if s_m > end_m or (s_m == end_m and s_d > end_d): 
        cnt = 0
        break

    if s_m < temp_m or (s_m == temp_m and s_d <= temp_d):
        if e_m > end_m or (e_m == end_m and e_d > end_d):
            end_m, end_d = e_m, e_d
            
            if end_m == 12 or i == N-1:
                cnt += 1
                break
    elif s_m < end_m or (s_m == end_m and s_d <= end_d):
        temp_m, temp_d = end_m, end_d
        cnt += 1
        continue          
    
    i += 1

if end_m == 12:
    print(cnt)
else:
    print(0)

