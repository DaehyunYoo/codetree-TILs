# A 학생의 수학, 영어 점수 입력 받기
math_a, eng_a = map(int, input().split())

# B 학생의 수학, 영어 점수 입력 받기
math_b, eng_b = map(int, input().split())

# 수학 점수 우선 비교
if math_a > math_b:
    print("A")
elif math_b > math_a:
    print("B")
# 수학 점수가 같은 경우 영어 점수 비교
else:
    if eng_a > eng_b:
        print("A")
    else:
        print("B")