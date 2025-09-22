def zodiac_sign(day, month):
    month = month.lower()
    if (month == "март" and day >= 21) or (month == "апрель" and day <= 19):
        return "Овен"
    elif (month == "апрель" and day >= 20) or (month == "май" and day <= 20):
        return "Телец"
    elif (month == "май" and day >= 21) or (month == "июнь" and day <= 20):
        return "Близнецы"
    elif (month == "июнь" and day >= 21) or (month == "июль" and day <= 22):
        return "Рак"
    elif (month == "июль" and day >= 23) or (month == "август" and day <= 22):
        return "Лев"
    elif (month == "август" and day >= 23) or (month == "сентябрь" and day <= 22):
        return "Дева"
    elif (month == "сентябрь" and day >= 23) or (month == "октябрь" and day <= 22):
        return "Весы"
    elif (month == "октябрь" and day >= 23) or (month == "ноябрь" and day <= 21):
        return "Скорпион"
    elif (month == "ноябрь" and day >= 22) or (month == "декабрь" and day <= 21):
        return "Стрелец"
    elif (month == "декабрь" and day >= 22) or (month == "январь" and day <= 19):
        return "Козерог"
    elif (month == "январь" and day >= 20) or (month == "февраль" and day <= 18):
        return "Водолей"
    elif (month == "февраль" and day >= 19) or (month == "март" and day <= 20):
        return "Рыбы"
    else:
        return "Некорректная дата"

day = int(input("Введите день рождения: "))
month = input("Введите месяц рождения: ")
print("Ваш знак зодиака:", zodiac_sign(day, month))
