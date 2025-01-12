A = input()
B = input()
cnt = 0
found = False

for i in range(len(A)):
    # 한 칸씩 오른쪽으로 밀기
    temp = A[-1] + A[:-1]  # 항상 마지막 문자 하나만 앞으로 가져옴
    cnt += 1
    
    if temp == B:
        found = True
        print(cnt)
        break
    A = temp  # 다음 반복을 위해 temp를 A에 저장

if not found:
    print(-1)