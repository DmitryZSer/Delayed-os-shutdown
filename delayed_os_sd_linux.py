from tkinter import *
from tkinter.messagebox import showerror
import os

app = Tk()
app.title("Delayed OS Shutdown")
app.geometry("400x60")
app.resizable(width=False, height=False)
app.configure(background='#1f75fe')

time_var = IntVar(value=0)

def update_time(delta):
    new_value = time_var.get() + delta
    if new_value < 0:
        new_value = 0
    time_var.set(new_value)

def delayed():
    time = time_var.get()
    if time < 1:
        showerror("Error", "Time must be at least 1 minute")
    else:
        os.system(f'shutdown -h +{time}')  

def clearTime():
    os.system('shutdown -c')

# Поле ввода
timeEntry = Entry(app, textvariable=time_var, validate="key", 
                 font=('Arial', 22), width=3)
timeEntry['validatecommand'] = (timeEntry.register(lambda inStr: inStr.isdigit()), '%S')
timeEntry.place(x=12, y=10)

# Кнопки "+/-"
increaseButton = Button(app, text='+', font=('Arial', 10), width=1, height=1,
                        command=lambda: update_time(10), bg='#7FBA00', bd=2)
increaseButton.place(x=80, y=15)

decreaseButton = Button(app, text='-', font=('Arial', 10), width=1, height=1,
                        command=lambda: update_time(-10), bg='#F25022', bd=2)
decreaseButton.place(x=127, y=15)

# Кнопки управления
setButton = Button(app, text='Set time', font=('Arial', 10), width=10, height=2, 
                   command=delayed, bg='#7FBA00', bd=2)
setButton.place(x=176, y=6)

clearTimeButton = Button(app, text='Clear time', font=('Arial', 10), width=10, height=2, 
                         command=clearTime, bg='#F25022', bd=2)
clearTimeButton.place(x=288, y=6)

app.mainloop()