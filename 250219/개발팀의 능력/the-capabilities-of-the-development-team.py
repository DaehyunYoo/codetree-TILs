nums = list(map(int, input().split()))

answer = 10**4
for i in range(len(nums)):
    for j in range(i, len(nums)):
        team1 = nums[i] + nums[j]
        for k in range(len(nums)):
            for t in range(k, len(nums)):
                if k != i and k != j and t != i and t != j:
                    team2 = nums[k] + nums[t]
                    team3 = sum(nums) - (team1 + team2)
                    if team1 != team2 != team3:
                        teams = [team1, team2, team3]
                        total = max(teams) - min(teams)

                        answer = min(answer, total)

print(answer)