word1 = input()
word2 = input()

word1 = sorted(word1)
word2 = sorted(word2)

result = True

if len(word1) != len(word2):
    result = False
else:
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            continue
        else:
            result = False
            break

if result:
    print('Yes')
else:
    print('No')