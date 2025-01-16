def calculate_sum(A, m):
    result = 0
    
    while m >= 1:  # m이 1일 때도 포함하도록 변경
        # 현재 m번째 원소를 더함
        result += A[m-1]
        
        # m 값 업데이트
        if m == 1:  # m이 1이면 종료
            break
        elif m % 2 != 0:  # m이 홀수면 1을 뺌
            m = m - 1
        else:  # m이 짝수면 2로 나눔
            m = m // 2
            
    return result

# 입력 받기
n, m = map(int, input().split())
A = list(map(int, input().split()))

# 결과 계산 및 출력
result = calculate_sum(A, m)
print(result)