import math
pi = 3.14
x = input('Введите x: ')
y = input("Введите y: ")
chisl = 3 * ((math.cos(int(x) - pi/6)) ** 2)
snam = 0.5 + math.sin(int(y)**2)
print(chisl/snam)
input()