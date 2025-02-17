# 변수 선언 및 입력
string = input()
n = len(string)

# (( )) 쌍의 개수를 셉니다
cnt = 0
for i in range(n):
    if string[i] == '(' and string[i+1] == '(':
        for j in range(i + 2, n-1):
            if string[j] == ')' and string[j+1] == ')':
                cnt += 1

print(cnt)