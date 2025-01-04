n = int(input())

nums = list(map(int, input().split()))

print(*[n * n for n in nums])