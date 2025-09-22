countries_temperature = []

print("Введите данные по странам. Для завершения \"\".")

while True:
    country = input("Название страны: ").strip()

    if country == "":
        break

    temps = list(map(float, input("Температуры (через пробел): ").split()))

    countries_temperature.append([country, temps])


print("\nВведённые данные:")
for item in countries_temperature:
    print(item)


print("Средняя температура в странах:")
for item in countries_temperature:

    temps_c =[]
    country = item[0]
    for temps_f in item[1]:
        temps_c.append((temps_f - 32) * 5 / 9)


    avg_temps_c = sum(temps_c) / len(temps_c)
    print(f"{country} - {avg_temps_c} C")

