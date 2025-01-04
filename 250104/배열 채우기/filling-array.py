numbers = []  # 입력받은 숫자들을 저장할 리스트

while True:
    # 공백을 기준으로 숫자들을 입력받음
    input_numbers = list(map(int, input().split()))
    
    for num in input_numbers:
        if num == 0:  # 0을 입력받으면
            print(*numbers[::-1])  # 지금까지 입력받은 숫자들 출력
            exit()  # 프로그램 종료
        numbers.append(num)  # 0이 아닌 숫자는 리스트에 추가