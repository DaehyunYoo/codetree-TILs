n = int(input())
cnt, cnt_a = 0, 0
for i in range(n):
    word = input()
    cnt += len(word)
    if word[0] == 'a':  # 첫 번째 문자가 'a'인 경우만 카운트
        cnt_a += 1

print(cnt, cnt_a)