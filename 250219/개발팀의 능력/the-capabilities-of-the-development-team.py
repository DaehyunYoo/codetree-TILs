def find_min_diff():
    nums = list(map(int, input().split()))
    n = len(nums)
    min_diff = float('inf')
    
    # 첫 번째 팀(2명) 선택
    for i in range(n):
        for j in range(i+1, n):
            team1 = nums[i] + nums[j]
            
            # 두 번째 팀(2명) 선택
            for k in range(n):
                for l in range(k+1, n):
                    # 첫 번째 팀과 겹치지 않는 경우만
                    if k != i and k != j and l != i and l != j:
                        team2 = nums[k] + nums[l]
                        
                        # 남은 1명이 세 번째 팀
                        remain_person = set(range(n)) - {i,j,k,l}
                        if len(remain_person) == 1:
                            team3 = nums[list(remain_person)[0]]
                            
                            # 모든 팀의 능력치가 서로 다른 경우만
                            if len(set([team1, team2, team3])) == 3:
                                teams = [team1, team2, team3]
                                diff = max(teams) - min(teams)
                                min_diff = min(min_diff, diff)
    
    return min_diff if min_diff != float('inf') else -1

print(find_min_diff())