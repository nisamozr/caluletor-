from  tkinter import *
from tkinter import Entry

add = ""
def callback(number):
   global add
   add = number
   value.set(add)



#GUI

window = Tk()
window.title("calculator")
window.geometry("400x500")
window.config(bg='#b4f0df')

value = StringVar()
input_field = Entry(window, textvariable='value')
input_field.place(height=100)
input_field.grid(columnspan=4, ipadx=100, ipady=5)
input_field.focus_set()


_1 = Button(window, text='1', fg='white', bg='black', bd=0,  height=2, width=7, command=lambda: callback(1))
_1.grid(row=2, column=0)
_2 = Button(window, text='2', fg='white', bg='black', bd=0,  height=2, width=7, command=lambda: callback(2))
_2.grid(row=2, column=1)
_3 = Button(window, text='3', fg='white', bg='black', bd=0,  height=2, width=7)
_3.grid(row=2, column=2)
_4 = Button(window, text='4', fg='white', bg='black', bd=0,  height=2, width=7)
_4.grid(row=3, column=0)
_5 = Button(window, text='5', fg='white', bg='black', bd=0,  height=2,width=7)
_5.grid(row=3, column=1)
_6 = Button(window, text='6', fg='white', bg='black', bd=0,  height=2, width=7)
_6.grid(row=3, column=2)
_7 = Button(window, text='7', fg='white', bg='black', bd=0,  height=2, width=7)
_7.grid(row=4, column=0)
_8 = Button(window, text='8', fg='white', bg='black', bd=0,  height=2, width=7)
_8.grid(row=4, column=1)
_9 = Button(window, text='9', fg='white', bg='black', bd=0,  height=2, width=7)
_9.grid(row=4, column=2)
_0 = Button(window, text='0', fg='white', bg='black', bd=0, height=2, width=7)
_0.grid(row=5, column=0)
plus = Button(window, text='+', fg='white', bg='black', bd=0,  height=2, width=7)
plus.grid(row=2, column=3)
minus = Button(window, text='-', fg='white', bg='black', bd=0,  height=2, width=7)
minus.grid(row=3, column=3)
multiply = Button(window, text='*', fg='white', bg='black', bd=0,  height=2, width=7)
multiply.grid(row=4, column=3)
divide = Button(window, text='/', fg='white', bg='black', bd=0,  height=2, width=7)
divide.grid(row=5, column=3)
equal = Button(window, text='=', fg='white', bg='black', bd=0,  height=2, width=7)
equal.grid(row=5, column=2)
clear = Button(window, text='Clear', fg='white', bg='black', bd=0, height=2, width=7)
clear.grid(row=5, column=1)



window.mainloop()