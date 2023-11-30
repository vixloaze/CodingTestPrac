from collections import deque
import sys

input = sys.stdin.readline

testcase = int(input())

for i in range(testcase):
    p = input().strip()
    n = int(input())
    numArray = input().strip()
    
    if n == 0:
        if 'D' in p:
            print("error")
        else:
            print("[]")
        continue
    
    array = deque(numArray[1:-1].split(",") if n > 0 else [])
    
    is_reversed = False
    error_flag = False
    
    for cmd in p:
        if cmd == "R":
            is_reversed = not is_reversed #한 번 이상 나올 경우 다시 한 번 False로 돌려야 함
        elif cmd == "D":
            if array:
                if is_reversed:
                    array.pop() ## 뒤에 원소 빠짐
                else: 
                    array.popleft() # 앞 원소 빠짐
            else:
                print("error")
                error_flag = True
                break
    
    if error_flag:
        continue
    
    result = list(array) if not is_reversed else list(reversed(array))
    print("[" +",".join(result)+"]")
            