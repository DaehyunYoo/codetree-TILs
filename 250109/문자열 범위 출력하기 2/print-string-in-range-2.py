given_str = input()
N = int(input())

for i in range(len(given_str)-1, len(given_str)-N-1, -1):
    print(given_str[i], end="")