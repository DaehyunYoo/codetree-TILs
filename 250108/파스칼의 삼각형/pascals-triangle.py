n = int(input())

arr = []

for i in range(n):
    arr.append([1] * (i+1))

for i in range(1,n):
    for j in range(1,i):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for i in range(n):
    print(*arr[i])