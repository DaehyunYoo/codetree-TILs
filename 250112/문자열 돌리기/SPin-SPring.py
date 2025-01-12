s = input()
L = len(s)

print(s)
for i in range(L):
    s = s[-1] + s[:-1]
    print(s)