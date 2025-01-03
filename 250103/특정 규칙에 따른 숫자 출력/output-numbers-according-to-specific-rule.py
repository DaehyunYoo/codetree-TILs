n = int(input())
cnt = 1

for i in range(n):
    # 공백 출력
    print("  " * i, end="")
    
    # 현재 줄의 숫자들 출력
    for j in range(n-i):
        print(cnt, end=" ")
        cnt = cnt % 9 + 1  # 9 다음에 1로 돌아가기
    print()  # 줄바꿈