a = input()

if (ord(a) - 1) < 97:
    print(chr(122))
else:
    print(chr(ord(a) - 1))