given_str = input()

while len(given_str) != 1:
    N = int(input())
    given_str = list(given_str)
    if len(given_str) > N:
        given_str.pop(N)
        print(''.join(given_str))
    else:
        given_str.pop(-1)
        print(''.join(given_str))