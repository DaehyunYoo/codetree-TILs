n = int(input())

# 각 줄에 대해
for i in range(n):
    # 공백 출력 (각 줄마다 i개의 공백)
    print("  " * i, end="") # 앞의 공백
    
    # 별 출력 ((2 * n) - (2 * i) - 1개의 별)
    stars = (2 * n) - (2 * i) - 1
    for j in range(stars):
        print("* ", end="")
        
    # 줄바꿈
    print()