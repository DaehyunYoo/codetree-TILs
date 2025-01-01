n = int(input())

# 각 줄에 대해
for i in range(n):
    # 홀수 번째 줄 (i가 짝수)
    if i % 2 == 0:
        print("*")
    # 짝수 번째 줄 (i가 홀수)
    else:
        # i + 1개의 별 출력
        for j in range(i + 1):
            print("*", end=" ")
        print()