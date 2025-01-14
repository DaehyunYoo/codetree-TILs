def is_subsequence(n1, n2, A, B):
    # 모든 가능한 시작 위치에 대해 검사
    for i in range(n1 - n2 + 1):
        # 현재 위치에서 B의 모든 원소와 일치하는지 확인
        match = True
        for j in range(n2):
            if A[i + j] != B[j]:
                match = False
                break
        # 모든 원소가 일치하면 True 반환
        if match:
            return "Yes"
    # 일치하는 부분을 찾지 못하면 False 반환
    return "No"

# 입력받기
n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 결과 출력
print(is_subsequence(n1, n2, A, B))