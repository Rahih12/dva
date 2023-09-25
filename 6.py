import math

x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
radius = float(input("Введите радиус круга: "))

distance = math.sqrt(x ** 2 + y ** 2)

if distance <= radius:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")
