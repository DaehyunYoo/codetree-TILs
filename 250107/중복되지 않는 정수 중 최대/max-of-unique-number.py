# 첫 번째 줄에서 N 입력받기
N = int(input())

# N개의 정수를 입력받아 리스트로 저장
numbers = list(map(int, input().split()))

# 각 숫자의 등장 횟수를 저장할 딕셔너리
count_dict = {}

# 각 숫자의 등장 횟수 계산
for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# 중복되지 않은 숫자들 중 최댓값 찾기
max_non_duplicate = -1
for num, count in count_dict.items():
    if count == 1 and num > max_non_duplicate:
        max_non_duplicate = num

# 결과 출력
print(max_non_duplicate)