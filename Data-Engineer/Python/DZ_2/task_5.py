car_ids = []

print("Введите номера авто по одному. Для завершения \"\".")

while True:
    num = input().strip()

    if num == "":
        break

    car_ids.append(num)

print("Введённые номера:", car_ids)

valid_letters = set("АВЕКМНОРСТУХ")

print("\nРезультат:")
for car_id in car_ids:
    is_valid = True

    if car_id[0] not in valid_letters:
        is_valid = False
    elif not car_id[1:4].isdigit():
        is_valid = False
    elif not all(char in valid_letters for char in car_id[4:6]):
        is_valid = False
    elif not car_id[6:].isdigit():
        is_valid = False

    if is_valid:
        print(f"Номер {car_id[:6]} валиден. Регион: {car_id[6:]}")
    else:
        print(f"Номер {car_id} не валиден")