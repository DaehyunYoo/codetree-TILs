N = int(input())

nums = list(map(int, input().split()))

def abs_num(x):

    return abs(x)

for i in nums:
    print(abs_num(i), end=" ")