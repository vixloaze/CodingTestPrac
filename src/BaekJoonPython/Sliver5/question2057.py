def my_factorial(n):
    if n==0 :
        return 1
    else:
        return n*(my_factorial(n-1))

fac_num = [my_factorial(i) for i in range(21)]

num = int(input())

if num == 0:
    print("NO")
else:
    for i in range(20, -1, -1):
        if num >= fac_num[i]:
            num -= fac_num[i]

    print("YES") if num == 0 else print("NO")

