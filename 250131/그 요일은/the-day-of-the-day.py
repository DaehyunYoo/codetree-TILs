def count_specific_weekday(m1, d1, m2, d2, target_day):
    month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 2024년은 윤년
    day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    # 시작일부터 목표일까지의 총 일수 계산
    total_days = 0
    curr_month, curr_day = m1, d1
    
    while True:
        if curr_month == m2 and curr_day == d2:
            break
            
        total_days += 1
        curr_day += 1
        
        # 월 바꾸기
        if curr_day > month_days[curr_month]:
            curr_day = 1
            curr_month += 1
    
    # 목표 요일의 인덱스 찾기
    target_index = day_of_week.index(target_day)
    
    # 시작일의 요일부터 목표 요일까지의 횟수 계산
    count = (total_days + 1) // 7  # 완전한 주의 수
    
    # 첫 주와 마지막 주의 부분 계산
    remaining_days = (total_days + 1) % 7
    start_index = 0  # 월요일부터 시작
    
    # 남은 날들 중 목표 요일이 있는지 확인
    for i in range(remaining_days):
        if (start_index + i) % 7 == target_index:
            count += 1
            break
    
    return count

# 입력 예시
m1, d1, m2, d2 = map(int, input().split())
target_day = input()  # 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun' 중 하나

result = count_specific_weekday(m1, d1, m2, d2, target_day)
print(result)