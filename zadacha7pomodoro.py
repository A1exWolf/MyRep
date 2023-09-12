# Создайте таймер, который будет измерять 25 минут работы и 5 минут отдыха, с
# возможностью установить количество циклов. Применяйте GUI
import tkinter as tk
import time

# Создаем главное окно
app = tk.Tk()
app.title("Помидоро Таймер")
app.geometry("200x200")

# Переменные для времени работы и отдыха (в секундах)
work_time = 0
break_time = 0
current_time = 0
cycles_completed = 0
is_work_time = True  # Флаг для определения, работаем ли мы сейчас или отдыхаем

# Функция для обновления таймера
def update_timer():
    global current_time, work_time, break_time, cycles_completed, is_work_time

    if current_time > 0:
        current_time -= 1
        time_display.config(text=f"Осталось времени: {current_time // 60}:{current_time % 60}")
        app.after(1000, update_timer)  # Вызываем эту функцию через 1 секунду
    else:
        if is_work_time:
            cycles_completed += 1
            cycles_label.config(text=f"Прошло циклов: {cycles_completed}")
            is_work_time = False
            current_time = break_time
            time_display.config(text=f"Отдых: {current_time // 60}:{current_time % 60}")
        else:
            is_work_time = True
            current_time = work_time
            time_display.config(text=f"Работа: {current_time // 60}:{current_time % 60}")

# Функция для запуска таймера
def start_timer():
    global current_time, work_time, break_time, cycles_completed, is_work_time
    work_time = float(work_entry.get()) * 60
    break_time = float(break_entry.get()) * 60
    current_time = work_time
    cycles_label.config(text=f"Прошло циклов: {cycles_completed}")
    is_work_time = True
    update_timer()

# Функция для сброса таймера
def reset_timer():
    global current_time, work_time, break_time, is_work_time
    current_time = 0
    work_time = 0
    break_time = 0
    is_work_time = True
    time_display.config(text="Осталось времени: 00:00")

# Создаем элементы управления
time_display = tk.Label(app, text="Осталось времени: 00:00")
work_label = tk.Label(app, text="Время работы (минут):")
work_entry = tk.Entry(app)
break_label = tk.Label(app, text="Время отдыха (минут):")
break_entry = tk.Entry(app)
start_button = tk.Button(app, text="Старт", command=start_timer)
reset_button = tk.Button(app, text="Сброс", command=reset_timer)
cycles_label = tk.Label(app, text=f"Прошло циклов: {cycles_completed}")

# Размещаем элементы на форме
time_display.pack()
work_label.pack()
work_entry.pack()
break_label.pack()
break_entry.pack()
start_button.pack()
reset_button.pack()
cycles_label.pack()

# Запускаем приложение
app.mainloop()
