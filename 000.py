from math import factorial
tot = 0
n = int(input('digite um numero inteiro :'))
m = factorial(n)
for c in range(1, n + 1,):
    if n % c == 0:
     print('\033[34m', end=' ')
     print('{}'.format(c), end=' ')
     tot += 1
    else:
     print('\033[33m', end=' ')
     print('{}'.format(c), end=' ')
print('\n\033[m o numero {} foi divisivel {} vezes '.format(n, tot))
if tot == 2:
  print('E por isso ele é PRIMO')
else:
    for d in range(n, 1):
        print('{} x'.format(d), end=' ')
    print('O fatorial do numero é {}'.format(m))
