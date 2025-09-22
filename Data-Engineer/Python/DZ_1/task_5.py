number = int(input())
sum1 = 0
sum2 = 0

number_t = number
for i in range(3):
    sum1 += number_t % 10
    number_t //= 10

temp = 100000
for i in range(3):
    sum2 += number_t / temp
    temp /= 10

print("Результат:")
if (sum1 == sum2):
    print("Счастливый билет")
else:
    print("Несчастливый билет")