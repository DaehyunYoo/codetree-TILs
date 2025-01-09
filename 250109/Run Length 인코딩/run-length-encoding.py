A = input()

result = []
cnt = 1
result.append(A[0])
for i in range(1, len(A)):
    if A[i-1] == A[i]:
        cnt += 1
    else:
        result.append(str(cnt))
        result.append(A[i])
        cnt = 1

result.append(str(cnt))

encoded = ''.join(result)
print(len(encoded))
print(encoded)