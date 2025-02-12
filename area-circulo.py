from math import pi

radio = float(input("Por favor, ingrese el radio del circulo: "))

area = pi * radio ** 2

print(f'El area del circulo con radio {radio} es: {round(area, 2)}')