n = int(input())
cnt, cnt_a = 0, 0
for i in range(n):
    word = input()
    cnt_a += word.count('a')
    cnt += len(word)

print(cnt, cnt_a)