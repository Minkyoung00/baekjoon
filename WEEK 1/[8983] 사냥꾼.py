def bin_search(A,animal):           # 가장 가까운 사대를 찾는 함수
    left = 0						#검색 범위 맨 앞 인덱스
    right = len(A) -1				#검색 범위 맨 뒤 인덱스
    x, y = animal[0],animal[1]
    while True:				
        center = (left+right) //2
        distance = abs(A[center] - x) + y
        if A[center] == x:		# 종료 조건 1. 거리(abs()) <= L
            return center			# 인덱스값 출력
        elif A[center] < x:
            left = center + 1
        else:
            right = center - 1
        if right < left:			# 종료 조건 2
            if left > M-1 or abs(x-A[right]) < abs(x-A[left]):
                return right
            else:
                return left 
					# 검색 실패

M, N, L = input().split()
M, N, L = int(M), int(N), int(L)    # M: 사대, N: 동물수, L: 사정거리
sadaes = sorted([int(i) for i in input().split()]) 
animals = []
for i in range(N):
    x, y = input().split()
    animals.append([int(x),int(y),False])

asw = 0
for animal in animals:
    if abs(animal[0]-sadaes[bin_search(sadaes,animal)])+animal[1] <= L:
        asw += 1

print(asw)