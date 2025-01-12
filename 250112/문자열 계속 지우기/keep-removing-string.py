A = input()
B = input()

while True:
    # 초기 문자열 길이 저장
    original_length = len(A)
    
    # 현재 위치부터 시작해서 부분문자열 중 B와 일치하는 문자열을 찾아 제거
    i = 0
    while i <= len(A) - len(B):
        # i번째 위치에서 시작하는 부분문자열이 B와 일치하면
        if A[i:i+len(B)] == B:
            # 해당 부분을 제거
            A = A[:i] + A[i+len(B):]
        else:
            i += 1
    
    # 더 이상 제거할 문자열이 없으면 종료
    if len(A) == original_length:
        break

# 최종 결과 출력
print(A)