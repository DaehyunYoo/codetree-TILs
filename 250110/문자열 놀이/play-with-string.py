# 입력 받기
s, q = input().split()
s = list(s)  # 문자열을 리스트로 변환
q = int(q)

# 각 쿼리 처리
for _ in range(q):
    query = input().split()
    op = query[0]
    
    if op == '1':
        # 위치 교환
        a, b = int(query[1]) - 1, int(query[2]) - 1  # 0-based index로 변환
        s[a], s[b] = s[b], s[a]  # 직접 swap
    else:  # op == '2'
        # 문자 변환
        a, b = query[1], query[2]
        for i in range(len(s)):
            if s[i] == a:
                s[i] = b
                
    # 각 쿼리 결과 출력
    print(''.join(s))