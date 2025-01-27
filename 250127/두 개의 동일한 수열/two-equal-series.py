n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
result = True

for i in range(len(A)):
    if A[i] != B[i]:
        result = False
        break
    else:
        result = True

if result:
    print('Yes')
else:
    print('No')