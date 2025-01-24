n = int(input())
nums = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def f(nums):
    if len(nums) == 1:
        return nums[0]
    return lcm(nums[0], f(nums[1:]))

print(f(nums))