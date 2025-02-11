a_x1, a_y1, a_x2, a_y2 = map(int, input().split())
b_x1, b_y1, b_x2, b_y2 = map(int, input().split())
m_x1, m_y1, m_x2, m_y2 = map(int, input().split())

# A, B 직사각형의 전체 넓이 계산
area_a = (a_x2 - a_x1) * (a_y2 - a_y1)
area_b = (b_x2 - b_x1) * (b_y2 - b_y1)

# M과 A의 겹치는 부분 계산
if m_x2 < a_x1 or a_x2 < m_x1 or m_y2 < a_y1 or a_y2 < m_y1:
    intersection_a = 0
else:
    width_a = min(a_x2, m_x2) - max(a_x1, m_x1)
    height_a = min(a_y2, m_y2) - max(a_y1, m_y1)
    intersection_a = width_a * height_a

# M과 B의 겹치는 부분 계산
if m_x2 < b_x1 or b_x2 < m_x1 or m_y2 < b_y1 or b_y2 < m_y1:
    intersection_b = 0
else:
    width_b = min(b_x2, m_x2) - max(b_x1, m_x1)
    height_b = min(b_y2, m_y2) - max(b_y1, m_y1)
    intersection_b = width_b * height_b

# 결과 출력: A와 B의 전체 넓이에서 M과 겹치는 부분을 뺌
result = area_a + area_b - intersection_a - intersection_b
print(result)