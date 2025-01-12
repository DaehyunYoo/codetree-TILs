A = input()
qu = input()

for i in range(len(qu)):
    if qu[i] == 'L':
        A = A[1:] + A[0]
    else:
        A = A[-1] + A[:-1]
print(A)