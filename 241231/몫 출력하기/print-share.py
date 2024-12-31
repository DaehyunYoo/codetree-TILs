even_count = 0  # 짝수를 처리한 횟수를 세는 변수

while True:
    num = int(input())  # 입력받기
    
    # 짝수인 경우에만 처리
    if num % 2 == 0:
        even_count += 1
        print(num // 2)  # 2로 나눈 몫 출력
    
    # 짝수를 3번 처리했다면 종료
    if even_count == 3:
        break