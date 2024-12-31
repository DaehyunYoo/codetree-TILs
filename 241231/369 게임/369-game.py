n = int(input())

for i in range(1, n+1):
    if '3' in list(str(i).split()) or '6' in list(str(i).split()) or '9' in list(str(i).split()):
        print(0, end=" ")
    else:
        print(i, end=" ")