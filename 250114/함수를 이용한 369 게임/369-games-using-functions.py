a, b = map(int, input().split())
cnt = 0
def func1(x):
    if '3' in str(x) or '6' in str(x) or '9' in str(x):
        return int(x)


def func2(x):
    if x % 3 == 0:
        return x
    
        

for i in range(a, b+1):
    if func1(i) or func2(i):
        cnt += 1

print(cnt)