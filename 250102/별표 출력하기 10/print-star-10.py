n = int(input())

for i in range(2 * n):
        # i가 짝수인 경우
        if i % 2 == 0:
            for _ in range(1 + i // 2):
                print('*', end=" ")
        # i가 홀수인 경우
        else:
            for _ in range(n - (i - 1) // 2):
                print('*', end=" ")
            
        print()