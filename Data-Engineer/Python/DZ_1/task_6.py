import math

figure = input("Введите тип фигуры (круг, треугольник, прямоугольник): ")

if figure == "круг":
    radius = float(input("Введите радиус круга: "))
    area = math.pi * radius ** 2
    print(f"Результат:\nПлощадь круга: {area:.2f}")

elif figure == "треугольник":
    a = float(input("Введите длину стороны A: "))
    b = float(input("Введите длину стороны B: "))
    c = float(input("Введите длину стороны C: "))

    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"Результат:\nПлощадь треугольника: {area:.2f}")

    else:
        print("Ошибка: треугольник с такими сторонами не существует!")

elif figure == "прямоугольник":
    length = float(input("Введите длину стороны A: "))
    width = float(input("Введите длину стороны B: "))
    area = length * width
    print(f"Результат:\nПлощадь прямоугольника: {area:.2f}")

else:
    print("Ошибка: неверный тип фигуры!")

