import sys
input= sys.stdin.readline

def oper(a,b,operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    else:    
        return int(a/b)
        
def ordering(oper_list):
    min_result = float("inf")
    max_result = float("-inf")
    result = []
    for i in oper_list:
        temp, j = A[0], 0
        not_visit = list(oper_list) # 방문 전 
        stack = [(i,[i])]
        while stack:
            u, order = stack.pop()
            
            if u in not_visit:
                order.append(u)
                temp = oper(temp,A[j+1],u)
                not_visit.remove(u)
                stack.extend(not_visit)
                j += 1

        max_result = max(temp,max_result)
        min_result = min(temp,min_result)

        result.append(order)
        
    print(max_result)
    print(min_result)    



N = int(input())    # 수의 개수
A = [int(i) for i in input().split()]  # 수 배열
hap, cha, gop, na  = [int(i) for i in input().split()]
oper_list = ['+']*hap + ['-']*cha + ["*"]*gop + ["//"]*na

ordering(oper_list)





