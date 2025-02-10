N = input()
N_2 = []
for i in N:
    N_2.append(i)

N_10 = 0
for i in range(len(N_2)):
    N_10 = N_10 * 2 + int(N_2[i])


N_10 = N_10 * 17

result = []
while True:
    if N_10 < 2:
        result.append(N_10)
        break
    
    result.append(N_10 % 2)
    N_10 //= 2

for i in result[::-1]:
    print(i, end='')