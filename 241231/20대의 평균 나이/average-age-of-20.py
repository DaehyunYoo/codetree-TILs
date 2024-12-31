lst = []
for _ in range(101):
    a = int(input())
    if 20 <= a < 30:
        lst.append(a)
    else:
        break

print(f'{sum(lst)/len(lst):.2f}')