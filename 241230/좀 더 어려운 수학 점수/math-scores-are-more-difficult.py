mid_score, final_score = map(int, input().split())

scholarship = 0

if mid_score >= 90:
    if final_score >= 95:
        scholarship = 100000
    elif final_score >= 90:
        scholarship = 50000

print(scholarship)