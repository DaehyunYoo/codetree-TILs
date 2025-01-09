words = []
for i in range(10):
    word = input()
    words.append(word)

word_1 = input()
result = []
for i in words:
    if i[-1] == word_1:
        result.append(i)


if not result:
    print('None')
else:
    for i in result:
        print(i)