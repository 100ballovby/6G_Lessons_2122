# если делится на 4, не делится на 100 или делится на 400
year = int(input('Введите год: '))

if (year % 4 == 0) and not(year % 100 == 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')



