import math
x = input('Введите радиус: ')
S = math.pi * (int(x)**2)

print(S - ((int(x))*2)**2/2)
input()