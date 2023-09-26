# задача 1. Палиндором
def palindrom(a):
    b = a.replace(" ",'').lower().strip()
    if b[::-1] == b:
        return 'Это палинтром'
    else:
        return "Это не палиндром"


print(palindrom(input('Введите значение: ')))