# Задача 2.Создайте простой таймер обратного отсчета, который будет отсчитывать время и
# выводить сообщение по истечении установленного периода времени.
import time

# time.sleep(2.5)

a = list(
    map(
        int,
        input(
            "Часы, минуты, секунды вас оповестить? (Пример 0 0 10 вводите через пробел 3 числа) "
        ).split(),
    )
)

a[0] = a[0] * 60 * 60
a[1] = a[1] * 60

summ = a[0] + a[1] + a[2]

i = 1
while i <= summ:
    time.sleep(1)
    print(f"Прошло {i} сек.")
    i += 1

print("Все пора!")
