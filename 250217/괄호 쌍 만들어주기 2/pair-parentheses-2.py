# 변수 선언 및 입력
string = input()
n = len(string)

# (( )) 쌍의 개수를 셉니다
cnt = 0
for i in range(n-1):  # n-1까지만 순회
    if string[i] == '(' and string[i+1] == '(':
        for j in range(i + 2, n-1):  # n-1까지만 순회
            if j+1 < n and string[j] == ')' and string[j+1] == ')':  # 범위 체크 추가
                cnt += 1
print(cnt)