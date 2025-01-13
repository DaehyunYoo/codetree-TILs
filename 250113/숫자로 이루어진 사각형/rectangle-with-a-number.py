N = int(input())

def square_(x):
    cnt = 1
    for i in range(x):
        for j in range(x):
            print(cnt, end=" ")
            if cnt == 9:
                cnt = 1
            else:
                cnt += 1
        print()

square_(N)