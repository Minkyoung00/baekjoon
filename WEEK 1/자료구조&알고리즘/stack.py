class FixedStack:
    class Empty(Exception):
        pass
    
    class Full(Exception):
        pass

    # 스택 객체가 생성될 때 호출되는 초기화 함수
    # 스택 크기를 capacity 파라미터로 받아 리스트형 배열 stk 생성
    # 스택 크기, 포인터 변수 선언&할당
    def __init__(self, capacity = 256):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    # FixedStack 객체 obj에 대해 len(obj)를 가능하게 해주는 스페셜메소드
    # 스택의 길이 return
    def __len__(self):
        return self.ptr
    
    def is_empty(self):
        return self.ptr <= 0

    def is_full(self):
        return self.ptr >= self.capacity

    def push(self, value):
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self,value):
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def clear(self):
        self.ptr = 0    

    def find(self,value):
        for i in range(self.ptr-1,-1,-1):
            if self.stk[i] == value:
                return i
        return -1
    
    def count(self, value):
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c
    
    # FixedStack 객체 obj에 대해 value in obj 를 가능하게 해주는 스페셜메소드
    # 값 포함 여부 bool값으로 return
    def __contains__(self, value):
        return self.count(value) > 0
    
    def dump(self):
        if self.empty():
            print('스택이 비어있습니다.')
        else:
            print(self.stk[:self.ptr])

    
    