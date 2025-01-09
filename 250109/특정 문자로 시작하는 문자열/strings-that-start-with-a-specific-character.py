n = int(input())
words = []
for i in range(n):
    a = input()
    words.append(a)

word = input()
cnt = 0
result = []
for i in words:
    if i[0] == word:
        cnt += 1
        result.append(len(i))

print(f'{cnt} {(sum(result)/len(result)):.2f}')

