import sys

n = int(input())

# 산술 평균
num_list = [int(sys.stdin.readline().strip()) for _ in range(n)]
mean = round(sum(num_list)/ len(num_list)) #소수점 계산 방지를 위해 반올림해야 함
print(mean) # 평균 출력

#중앙값
les = len(num_list)

list_sorted = sorted(num_list)
median = (list_sorted[n//2]+list_sorted[n//2-1]/2 if n%2==0 else list_sorted[n//2])
print(median) # 중앙값 출력

# 최빈값
dic = dict()
for i in list_sorted: # 빈도수 구하기
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

mx = max(dic.values()) #빈도수 중 최대값 구하기
mx_dic=[] # 최빈값 숫자 저장할 배열

for i in dic: 
    if mx == dic[i]:
        mx_dic.append(i)

if len(mx_dic) > 1:
    print(mx_dic[1])
else:
    print(mx_dic[0])
    
#범위
print(max(list_sorted)-min(list_sorted))