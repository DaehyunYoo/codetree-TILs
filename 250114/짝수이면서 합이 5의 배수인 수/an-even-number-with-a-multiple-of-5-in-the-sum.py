n = int(input())

def quiz(x):
    if x % 2 == 0 and (int(str(x)[0]) + int(str(x)[1])) % 5 == 0:
        return 'Yes'
    else:
        return 'No'

print(quiz(n))