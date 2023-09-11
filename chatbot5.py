#Реализуйте простого чат-бота, который может отвечать на базовые вопросы или
#играть в текстовые игры типа "20 вопросов" или "угадай число".
import random

def randChislo():
    while True:
        myRange = input("Какой диапазон чисел будет использовать от 1 до ")
        try:
            myRange = int(myRange)
            break
        except ValueError:
            print('Это не число, либо оно написано с ошибкой')

    while True:
        anw = input(f'Вы уверены? Диапазон от 1 до {myRange}. Оставляем? (Д/Н): ')
        if anw == "Д":
            break
        elif anw == "Н":
           while True:
               myRange = input('Введите новое число: ')
               try:
                   myRange = int(myRange)
                   break
               except ValueError:
                   print('Это не число, либо оно написано с ошибкой')
        else:
            print("Ответ некорректный")

    randoChislo = random.randint(1,myRange+1)
    popitok = 1
    print(f'Я загадал число от 1 до {myRange} теперь отгадывай ;) - ')
    while True:
        answer = input("Число - ")
        try:
            answer = int(answer)
            if int(answer) == randoChislo:
                print(f'Подзравляю ты отгадал число {randoChislo}. C {popitok} раза!')
                break
            elif int(answer) > myRange or int(answer) < 1:
                print('Это число не входит в диапазон')
            elif int(answer) > randoChislo:
                print('Загаданное число меньше!')
            elif int(answer) < randoChislo:
                print('Загаданное число больше!')
            popitok += 1
        except ValueError:
            print('Ты ввел не число попытайся еще!')

def twentQuestion():
    pass

print('Привет!')
name = input('Как тебя зовут?(Введи имя) ')

while True:
    print(f'{name} в какую игру ты хочешь поиграть?')
    print('''1. Угадай число
2. 20 вопросов
Напиши номер игры!
Если хочешь закончить играть напиши - "пока"''')
    numberGame = input()
    if numberGame == "1":
        randChislo()
    elif numberGame == "2":
        twentQuestion()
    elif numberGame.lower() == "пока":
        print("Пока. Приходите еще!")
        break
    else:
        print('Такой игры нет, либо функционал не распознан!')


