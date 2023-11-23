n,m = map(int, input().split())

eng_arr = input().split()
eng_arr.sort()

vowel = ['a','e','i','o','u']

def check(arr):
    v_cnt, c_cnt = 0, 0
    
    for i in arr:
        if i in vowel:
            v_cnt += 1
        else:
            c_cnt += 1
    
    if v_cnt >= 1 and c_cnt >= 2:
        return True
    else:
        return False

def back(arr):
    if len(arr) == n: # 배열 길이 
        if check(arr):
            print("".join(arr))
            return
    
    for i in range(len(arr), m):
        if arr[-1] < eng_arr[i]:
            arr.append(eng_arr[i])
            back(arr)
            arr.pop()


for i in range(m - n + 1):
    a = [eng_arr[i]]
    back(a)
