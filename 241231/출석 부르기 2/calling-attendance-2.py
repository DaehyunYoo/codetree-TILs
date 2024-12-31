# 학생 이름 매핑
students = {
    1: "John",
    2: "Tom",
    3: "Paul",
    4: "Sam"
}

# 입력을 받고 처리
while True:
    number = int(input())
    
    # 학생 번호가 유효한지 확인
    if number in students:
        print(students[number])
    else:
        print("Vacancy")
        break