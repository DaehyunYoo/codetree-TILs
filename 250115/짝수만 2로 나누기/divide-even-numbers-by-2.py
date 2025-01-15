N = int(input())

nums = list(map(int, input().split()))

def modify(x):
    if x % 2 == 0:
        return x // 2
    else:
        return x

for i in nums:
    print(modify(i), end=" ")
    