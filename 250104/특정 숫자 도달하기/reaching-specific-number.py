numbers = list(map(int, input().split()))
result = []
    
# 250 미만의 숫자들만 결과 리스트에 추가
for num in numbers:
    if num >= 250:
        break
    result.append(num)

# 합계와 평균 계산
total = sum(result)
average = total / len(result)

print(total, average)