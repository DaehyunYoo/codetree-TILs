n, q = map(int, input().split())

nums = list(map(int, input().split()))

for i in range(q):
    question = list(map(int, input().split()))
    if question[0] == 1:
        print(nums[question[1]-1])
    elif question[0] == 2:
        if question[1] in nums:
            print(nums.index(question[1])+1)
        else:
            print(0)
    else:
        print(*nums[question[1]-1:question[2]])


