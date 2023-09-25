a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a == b or b == c or a == c:
    print("Ошибка: есть равные числа")
else:
    if (a > b and a < c) or (a > c and a < b):
        print("Среднее число:", a)
    elif (b > a and b < c) or (b > c and b < a):
        print("Среднее число:", b)
    else:
        print("Среднее число:", c)
