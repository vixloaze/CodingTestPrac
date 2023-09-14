E, S, M = map(int, input().split())  # E, S, M 값을 입력받습니다.

year = 1  # 시작 년도를 1로 초기화합니다.

while True:
    if (year % 15 == E or (year % 15 == 0 and E == 15)) and \
       (year % 28 == S or (year % 28 == 0 and S == 28)) and \
       (year % 19 == M or (year % 19 == 0 and M == 19)):
        break  # 주어진 조건에 맞는 년도를 찾으면 반복문을 종료합니다.
    year += 1

print(year)  # 찾은 년도를 출력합니다.
