n, k, T = input().split()
word = []
for i in range(int(n)):
    w = input()
    if w[:len(T)] == T:
        word.append(w)

word.sort()

print(word[int(k)-1])