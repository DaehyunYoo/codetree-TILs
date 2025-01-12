s, q = input().split()

for i in range(int(q)):
    a = int(input())
    if a == 1:
        s = s[1:] + s[0]
        print(s)
    elif a == 2:
        s = s[-1] + s[:-1]
        print(s)
    else:
        new_s = ''
        for j in range(len(s)-1, -1, -1):
            new_s += s[j]
        s = new_s
        print(s)