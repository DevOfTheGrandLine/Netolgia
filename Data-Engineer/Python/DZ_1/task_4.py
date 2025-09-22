width = int(input())
length = int(input())
height = int(input())

if width <= 15 and length <= 15 and height <= 15:
    print("Коробка №1")
elif width > 200 or length > 200 or height > 200:
    print("Упаковка для лыж")
elif (15 < width < 50) or (15 < length < 50) or (15 < height < 50):
    print("Коробка №2")
else:
    print("Коробка №3")

