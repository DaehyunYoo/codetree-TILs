A, B = map(int, input().split())
N = int(input())

num = []
new_N = 0
for i in str(N):
    num.append(i)

for i in range(len(num)):
    new_N = new_N * A + int(num[i])

N = new_N


digits = []
while True:
    if N < B:
        digits.append(N)
        break
    
    digits.append(N % B)
    N //= B

for digit in digits[::-1]:
    print(digit, end='')