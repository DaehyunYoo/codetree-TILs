given_str = input()

result = ""
for i in range(1, len(given_str), 2):  # 홀수 인덱스(짝수 번째 문자)만 선택
    result = given_str[i] + result      # 역순으로 만들기 위해 앞에 추가

print(result)