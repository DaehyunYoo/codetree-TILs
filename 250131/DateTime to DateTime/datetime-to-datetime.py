a, b, c = map(int, input().split())
d, h, m = 11, 11, 11

# 입력된 시간이 시작 시간보다 이전인지 확인
if a < 11 or (a == 11 and b < 11) or (a == 11 and b == 11 and c < 11):
    print(-1)
else:
    # 시작 시간을 분으로 변환
    start_minutes = d * 24 * 60 + h * 60 + m
    # 종료 시간을 분으로 변환
    end_minutes = a * 24 * 60 + b * 60 + c
    
    # 차이 계산
    time_diff = end_minutes - start_minutes
    print(time_diff)