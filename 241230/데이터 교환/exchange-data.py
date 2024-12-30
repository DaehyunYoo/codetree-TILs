# 초기 값 설정
a = 5
b = 6
c = 7

# 값을 교환
temp = a  # a의 값을 임시 변수에 저장
a = c     # c의 값을 a에 저장
c = b     # b의 값을 c에 저장
b = temp  # 임시 변수에 저장된 a의 값을 b에 저장

# 결과 출력
print(a)
print(b)
print(c)