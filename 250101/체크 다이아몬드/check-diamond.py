n = int(input())

for i in range(n):
    line = ""
    for j in range(n - i - 1):
        line += " "
    for j in range(i + 1):
        line += "* " if j % 2 == 0 else "  "
    print(line.rstrip())

# 다이아몬드 아랫부분
for i in range(n - 1):
    line = ""
    for j in range(i + 1):
        line += " "
    for j in range(n - i - 1):
        line += "* " if j % 2 == 0 else "  "
    print(line.rstrip())