while True:
    x = input()
    if x == 'END':
        break
    else:
        for i in range(len(x)-1, -1, -1):
            print(x[i], end='')
        print()
