"""Exercício Python 51: Desenvolva um programa que leia o primeiro termo
e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão."""

t = int(input('primeiro termo:'))
r = int(input('razão :'))
d = t + (10-1) * r  # decimo termo
for c in range(t, d + r, r):
    print(c, end=' -> ')
print('ACABOU')