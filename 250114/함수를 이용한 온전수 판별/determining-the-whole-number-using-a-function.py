a, b = map(int, input().split())
cnt = 0

def num(x):
    # 짝수인 경우
    if x % 2 == 0:
        return False
    
    # 끝자리가 5인 경우
    if str(x)[-1] == '5':
        return False
    
    # 3의 배수이면서 9의 배수가 아닌 경우
    if x % 3 == 0 and x % 9 != 0:
        return False
    
    # 모든 조건을 통과한 경우
    return True

for i in range(a, b+1):
    if num(i):
        cnt += 1

print(cnt)