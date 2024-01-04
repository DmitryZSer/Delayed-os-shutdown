from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo

import os

#pyinstaller.exe --onefile --noconsole  --icon 'red_win.ico' .\delayed_os_sd.py --name 'Delayed os shutdown'

app = Tk()
# window.overrideredirect(True)
app.title("Delayed os shutdown")

app.geometry("300x60")
app.resizable(width=False, height=False)
app.configure(background='#1f75fe')



def testVal(inStr, acttyp):
    if acttyp == '1':
        if not inStr.isdigit():
            return False
    return True


timeEntry = Entry(app, validate="key", font='Times 22', width= 3)
timeEntry['validatecommand'] = (timeEntry.register(testVal), '%P', '%d')

def foo(e):
    s = timeEntry.get().strip()
    s = s[-1] if s in range(0,9) else ''
    timeEntry.delete ('3',END)
    timeEntry.insert(INSERT,s)

timeEntry.bind('<KeyRelease>',foo)

timeEntry.place(x=17, y=13)


def delayed():
    time = timeEntry.get()
    if time == "":
        showerror(title="Error", message="Input field is empty")
    else:
        try:
            time = int(time)
        except ValueError:
            showerror(title="Error", message="Invalid input")
        else:
            if time < 1:
                showerror(title="Error", message="Invalid input")
            else:
                time = time * 60
                os.system(f'shutdown -s -t {time}')


setButton = Button(app, text='Set time', height=2, width=13, command=delayed, background='#7FBA00', border='2px')
setButton.place(x=80, y=10)

def cleatTime():
    os.system('shutdown -a')

cleatTimeButton = Button(app, text='Clear time', height=2, width=13, command=cleatTime, background='#F25022', border='2px')
cleatTimeButton.place(x=190, y=10)



app.mainloop()