n = int(input())

classroom = 0  # 교실 (2일마다)
corridor = 0   # 복도 (3일마다)
bathroom = 0   # 화장실 (12일마다)

for day in range(1, n+1):  # 0일은 제외하고 1일부터 시작
   if day % 12 == 0:  # 12일마다 (가장 긴 주기)
       bathroom += 1
   elif day % 3 == 0:  # 3일마다
       corridor += 1
   elif day % 2 == 0:  # 2일마다
       classroom += 1

print(classroom, corridor, bathroom)