n = int(input())

for i in range(n):
    for j in range(n):
        # 첫 줄, 마지막 줄, 또는 첫 열, 마지막 열인 경우 별 출력
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*', end=' ')
        # i번째 행까지는 별을 출력 (테두리 안쪽)
        elif j < i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()