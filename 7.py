choice = int(input("Выберите фигуру: 1 - прямоугольник, 2 - треугольник, 3 - круг: "))

if choice == 1:
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))
    area = length * width
    print("Площадь прямоугольника:", area)
elif choice == 2:
    base = float(input("Введите длину основания треугольника: "))
    height = float(input("Введите высоту треугольника: "))
    area = 0.5 * base * height
    print("Площадь треугольника:", area)
elif choice == 3:
    radius = float(input("Введите радиус круга: "))
    area = 3.14159 * radius ** 2
    print("Площадь круга:", area)
else:
    print("Неверный выбор фигуры")
