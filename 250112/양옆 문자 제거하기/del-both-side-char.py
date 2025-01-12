given_str = input()

given_str = list(given_str)

given_str.pop(1)
given_str.pop(-2)
print(''.join(given_str))