k = int(input())

brack = list(input().split())
visited = [False]* 10
ans=[]

def check(num1, num2, k):
    if k =="<":
        return num1 < num2
    else:
        return num1 > num2

def dfs(iter, temp):
    if iter == k+1:
        ans.append(temp)
        return
    
    for i in range(10):
        if not visited[i]:
            if iter == 0 or check(temp[-1], str(i), brack[iter -1]):
                visited[i] = True
                dfs(iter +1, temp + str(i))
                visited[i] = False

dfs(0, "")

print(ans[-1])
print(ans[0])