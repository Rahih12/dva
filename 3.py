bigger = int(input("Введите большее число: "))
smaller = int(input("Введите меньшее число: "))

if bigger % smaller == 0:
    print(bigger, "кратно", smaller)
else:
    print(bigger, "не кратно", smaller)
    remainder = bigger % smaller
    print("Остаток от деления:", remainder)
