nums = list(map(int, input().split()))

opp = sum(nums[0: len(nums): 2])
epp = sum(nums[1: len(nums): 2])

print(opp - epp if opp > epp else epp - opp)