def check_counts(guess, answer):
    # 스트라이크(같은 위치, 같은 숫자)와 볼(다른 위치, 같은 숫자) 카운트
    guess_str = str(guess)
    answer_str = str(answer)
    
    strike = 0
    ball = 0
    
    # 스트라이크 체크
    for i in range(3):
        if guess_str[i] == answer_str[i]:
            strike += 1
    
    # 볼 체크
    for i in range(3):
        if guess_str[i] in answer_str and guess_str[i] != answer_str[i]:
            ball += 1
            
    return strike, ball

def is_valid_number(num):
    # 유효한 3자리 수인지 확인 (서로 다른 숫자로 구성)
    num_str = str(num)
    if len(num_str) != 3:
        return False
    return len(set(num_str)) == 3 and '0' not in num_str

N = int(input())
queries = []
for _ in range(N):
    num, cnt1, cnt2 = map(int, input().split())
    queries.append((num, cnt1, cnt2))

possible_answers = []
# 123부터 987까지 모든 가능한 수 체크
for num in range(123, 988):
    if not is_valid_number(num):
        continue
        
    # 모든 쿼리에 대해 조건을 만족하는지 확인
    valid = True
    for query, strike, ball in queries:
        s, b = check_counts(query, num)
        if s != strike or b != ball:
            valid = False
            break
    
    if valid:
        possible_answers.append(num)

print(len(possible_answers))