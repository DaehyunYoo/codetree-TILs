a_x1, a_y1, a_x2, a_y2 = map(int, input().split())
b_x1, b_y1, b_x2, b_y2 = map(int, input().split())

# 겹치는 구간이 없을 때
if b_y2 < a_y1 or b_x2 < a_x1 or b_x1 > a_x2 or b_y1 > a_y2:
    result = abs(a_x2 - a_x1) * abs(a_y2 - a_y1)

else:
    # 겹치는 구간이 있을 때
    original_width = abs(a_x2 - a_x1)
    original_height = abs(a_y2 - a_y1)
    min_area = float('inf')
    
    # 왼쪽으로 완전히 밀 경우
    area = original_height * original_width
    min_area = min(min_area, area)
    
    # 오른쪽으로 완전히 밀 경우
    area = original_height * original_width
    min_area = min(min_area, area)
    
    # 위로 완전히 밀 경우
    area = original_height * original_width
    min_area = min(min_area, area)
    
    # 아래로 완전히 밀 경우
    area = original_height * original_width
    min_area = min(min_area, area)
    
    result = min_area

print(result)