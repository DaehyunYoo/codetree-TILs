scores = list(input().split())

total = 0
for i in scores:
    total += float(i)

print(f"{(total / 8):.1f}")