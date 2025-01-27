n = int(input())

words = []
for _ in range(n):
    w = input()
    words.append(w)

words.sort()

for i in words:
    print(i)