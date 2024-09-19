from collections import deque

def solution(queue1, queue2):
    que1 = deque(queue1)
    que2 = deque(queue2)
    sum1 = sum(que1)
    sum2 = sum(que2)
    answer = 0

    for i in range((len(que1)+len(que2))*2):
        if sum1 > sum2:
            temp = que1.popleft()
            que2.append(temp)
            sum1 -= temp
            sum2 += temp

        elif sum1 < sum2:
            temp = que2.popleft()
            que1.append(temp)
            sum2 -= temp
            sum1 += temp
        
        else:
            return answer
        answer += 1

    return -1