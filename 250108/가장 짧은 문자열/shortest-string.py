word1 = input()
word2 = input()
word3 = input()

lst = [len(word1), len(word2), len(word3)]

print(max(lst) - min(lst))