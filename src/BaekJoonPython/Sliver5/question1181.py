import sys

num = int(input())

str_arr = []

for i in range(num):
    str_arr.append(sys.stdin.readline().strip())

str_arr.sort()
str_arr.sort(key=len)

str_arr = list(dict.fromkeys(str_arr))

for i in range(len(str_arr)):
    print(str_arr[i])