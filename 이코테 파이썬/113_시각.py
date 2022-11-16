# 정수 n 입력
# 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중
# 3이 하나라도 포함되는 경우의 수

time = int(input())

cnt = 0
for i in range(time+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                cnt += 1

print(cnt)
