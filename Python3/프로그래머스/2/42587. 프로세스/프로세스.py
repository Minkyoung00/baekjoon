def solution(priorities, location):
    answer = 0
    while priorities:
        front = priorities.pop(0)
        
        if location == 0:
            if len(priorities) == 0 or front >= max(priorities):
                answer += 1
                break
            else:
                priorities.append(front)
                location = len(priorities)
        else:
            if front >= max(priorities):
                answer += 1
            else:
                priorities.append(front)  
        location -= 1;        
        
    return answer