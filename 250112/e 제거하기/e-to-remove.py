words = input()

idx = words.find('e')
print(words[:idx] + words[idx+1:])