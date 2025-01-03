n = int(input())

for i in range(n):
    # 공백 출력
    print("  " * i, end="")
    
    # 현재 줄의 숫자들 출력
    for j in range(n - i, 0, -1):
        print(j, end=" ")
    print()  # 줄바꿈