gender = int(input())

age = int(input())

if gender == 0 and age >= 19:
    print('MAN')
elif gender == 0 and age < 19:
    print('BOY')
elif gender == 1 and age < 19:
    print('GIRL')
else:
    print('WOMAN')
