A = input()
B = input()
cnt = 0
found = False

for i in range(len(A)):
    temp = A[-i:] + A[:-i]
    cnt += 1
    if temp == B:
        found = True
        print(cnt)
        break
    A = temp

if not found:
    print(-1)
