# 중간고사와 기말고사 점수 입력받기
mid_score, final_score = map(int, input().split())

# 장학금 계산하기
scholarship = 0

# 중간고사가 90점 이상인 경우에만 기말고사 점수에 따라 장학금 지급
if mid_score >= 90:
    if final_score >= 95:
        scholarship = 100000  # 95점 이상이면 10만원
    elif final_score >= 90:
        scholarship = 50000   # 90점 이상이면 5만원
    # 그 외의 경우는 장학금 0원 (이미 0으로 초기화되어 있음)

# 장학금 출력
print(scholarship)