def bin_search(A,key):
    left = 0						#검색 범위 맨 앞 인덱스
    right = len(A) -1				#검색 범위 맨 뒤 인덱스

    while True:				
        center = (left+right) //2
        if A[center] == key:		# 종료 조건 1  
            return center			# 인덱스값 출력
        elif A[left] < key:
            left = center + 1
        else:
            right = center - 1
        if right < left:			# 종료 조건 2
            break
    return None						# 검색 실패

print(bin_search([1,2,3,5,7,8,9],0))
            