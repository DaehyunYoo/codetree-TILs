given_str = input()
N = int(input())

if N > len(given_str):
    print(given_str)
else:
    for i in range(len(given_str)-1, len(given_str)-N-1, -1):
        print(given_str[i], end="")