import sys
input = sys.stdin.readline

def oper(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    else:  # operator == "//"
        return int(a / b)

def ordering(operators):
    min_result =  1e9
    max_result =  -1e9
    
    stack = [(A[0], 0, operators)]
    
    while stack:
        value, index, remaining = stack.pop()
        
        if index == len(A) - 1:
            max_result = max(value, max_result)
            min_result = min(value, min_result)
            continue
        
        for i in range(len(remaining)):
            next_ops = remaining[:i] + remaining[i+1:]
            next_value = oper(value, A[index + 1], remaining[i])
            stack.append((next_value, index + 1, next_ops))
    
    print(max_result)
    print(min_result)

N = int(input())    # 수의 개수
A = list(map(int, input().split()))  # 수 배열
hap, cha, gop, na  = map(int, input().split())
operators = ['+'] * hap + ['-'] * cha + ["*"] * gop + ["//"] * na

ordering(operators)
