numbers = list(map(int, input().split()))
result = []
    
# 2500 미만의 숫자들만 결과 리스트에 추가
for num in numbers:
    if num >= 250:
        break
    result.append(num)

# 결과가 없는 경우 처리
if not result:
    print(0, 0)

# 합계와 평균 계산
total = sum(result)
average = total / len(result)

print(total, average)