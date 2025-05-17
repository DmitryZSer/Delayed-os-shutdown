from tkinter import *
from tkinter.messagebox import showerror
import os

app = Tk()
app.title("Delayed os shutdown")
app.geometry("370x60")
app.resizable(width=False, height=False)
app.configure(background='#1f75fe')
# app.iconbitmap('red_win.ico')  # Устанавливаем иконку окна

# Переменная для хранения времени
time_var = IntVar(value=0)

def update_time(delta):
    """Обновляет значение времени с учетом шага."""
    new_value = time_var.get() + delta
    if new_value < 0:
        new_value = 0  # Минимальное значение — 0
    time_var.set(new_value)

def delayed():
    """Выполняет отложенное выключение системы."""
    time = time_var.get()
    if time < 1:
        showerror(title="Error", message="Time must be at least 1 minute")
    else:
        os.system(f'shutdown -s -t {time * 60}')

def clearTime():
    """Отменяет запланированное выключение."""
    os.system('shutdown -a')

# Поле ввода времени
timeEntry = Entry(app, textvariable=time_var, validate="key", font='Times 22', width=3)
timeEntry['validatecommand'] = (timeEntry.register(lambda inStr: inStr.isdigit()), '%S')
timeEntry.place(x=17, y=12)

# Кнопка "Увеличить время"
increaseButton = Button(app, text='+', height=1, width=2, command=lambda: update_time(10), background='#7FBA00', border='2px')
increaseButton.place(x=74, y=18)

# Кнопка "Уменьшить время"
decreaseButton = Button(app, text='-', height=1, width=2, command=lambda: update_time(-10), background='#F25022', border='2px')
decreaseButton.place(x=105, y=18)

# Кнопка "Set time"
setButton = Button(app, text='Set time', height=2, width=13, command=delayed, background='#7FBA00', border='2px')
setButton.place(x=140, y=10)

# Кнопка "Clear time"
clearTimeButton = Button(app, text='Clear time', height=2, width=13, command=clearTime, background='#F25022', border='2px')
clearTimeButton.place(x=250, y=10)

app.mainloop()