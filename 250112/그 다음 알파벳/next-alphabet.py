a = input()

if (ord(a) + 1) > 122:  # 122는 'z'의 ASCII 값
    print(chr(97))      # 97은 'a'의 ASCII 값
else:
    print(chr(ord(a) + 1))