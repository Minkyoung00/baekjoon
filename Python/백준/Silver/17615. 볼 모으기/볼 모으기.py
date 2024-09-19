N = int(input())
balls = input()
balls_ = [1]

temp = 1
for i in range(1, len(balls)):
    if balls[i-1] == balls[i]:
        temp += 1
        balls_[-1] = temp
    else:
        temp = 1
        balls_.append(temp)

cnt = 0

if len(balls_) > 2:
    even = odd = 0

    if len(balls_) % 2: # 홀수
        for i in range(1, len(balls_)-1):
            if i % 2 == 0:
                even += balls_[i]
            else:
                odd += balls_[i]
        even += min(balls_[0], balls_[-1])

    else:
        for i in range(1, len(balls_)-1):
            if i % 2 == 0:
                even += balls_[i]
            else:
                odd += balls_[i]
    
    cnt = min (even, odd)

print(cnt)