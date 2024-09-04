def distance(a, b):
    if a % 3 == 0:
        a_n = a // 3 - 1
        a_k = 3
    else:
        a_n = a // 3
        a_k = a % 3

    if b % 3 == 0:
        b_n = b // 3 - 1
        b_k = 3
    else:
        b_n = b // 3
        b_k = b % 3

    return abs(a_n - b_n) + abs(a_k - b_k)
def solution(numbers, hand):
    answer = ''

    left = 10
    right = 12
    
    for i in numbers:
        if i == 0:
            i = 11
        if i in [1, 4, 7]:
            answer += "L"
            left = i
        elif i in [3, 6, 9]:
            answer += "R"
            right = i
        else:
            if distance(i, left) < distance(i,right):
                answer += "L"
                left = i
            elif distance(i, left) > distance(i,right):
                answer += "R"
                right = i
            else:
                if hand == "left":
                    answer += "L"
                    left = i
                else:
                    answer += "R"
                    right = i

    return answer