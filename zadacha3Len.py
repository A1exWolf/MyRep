#Напишите скрипт, который считает количество слов в введенной пользователем
#строке.
a = input("Введите строку ")
b = a.strip()
count = 1
if len(b) == 0:
    print('Строка пустая')
else:
    for i in b:
        if i == ' ':
            count += 1
    print(count)