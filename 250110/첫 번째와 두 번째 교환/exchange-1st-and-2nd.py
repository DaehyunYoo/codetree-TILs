given_str = input()
result = ''
for i in range(len(given_str)):
    if given_str[i] == given_str[0]:
        result += given_str[1]
    elif given_str[i] == given_str[1]:
        result += given_str[0]
    else:
        result += given_str[i]

print(result)