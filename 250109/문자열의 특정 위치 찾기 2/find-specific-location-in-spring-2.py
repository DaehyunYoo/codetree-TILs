a = input()
cnt = 0
lst = ["apple", "banana", "grape", "blueberry", "orange"]
for i in lst:
    if a == i[2] or a == i[3]:
        cnt += 1
        print(i)

print(cnt)