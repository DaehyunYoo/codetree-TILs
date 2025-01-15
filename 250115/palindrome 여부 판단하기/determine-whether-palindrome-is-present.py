A = input()

def palin(x):
    y = ''
    for i in range(len(x)-1, -1, -1):
        y += x[i]
    
    return y

if A == palin(A):
    print('Yes')
else:
    print('No')