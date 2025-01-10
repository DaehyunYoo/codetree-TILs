given_inp = input()
given_obj = input()

if given_obj in given_inp:
    print(given_inp.index(given_obj))
else:
    print(-1)