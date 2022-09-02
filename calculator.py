from tkinter import *

root = Tk()
root.title('Calculator')


# Numeric buttons

entry = Entry(root, width=42)
entry.grid(row=0, column=0, columnspan=3, pady=10)

def equal_func():

    # equal func
    entry.delete(0,END)


def func(x):
    global line
    line = entry.get()
    entry.delete(0, END)
    entry.insert(0,line+str(x))


def plus_func(): # minus func
    res = 0 + int(entry.get())
    entry.delete(0,END)


def clear_func():
    entry.delete(0, END)
    # global plus_list
    plus_list=[]
    return plus_list


zero = Button(root, text='0', padx=35, pady=15,command=lambda: func(0))
zero.grid(row=4, column=0)
one = Button(root, text='1', padx=35, pady=15,command=lambda: func(1))
one.grid(row=1, column=0)
two = Button(root, text='2', padx=35, pady=15,command=lambda: func(2))
two.grid(row=1, column=1)
three = Button(root, text='3', padx=35, pady=15,command=lambda: func(3))
three.grid(row=1, column=2)
four = Button(root, text='4', padx=35, pady=15,command=lambda: func(4))
four.grid(row=2, column=0)
five = Button(root, text='5', padx=35, pady=15,command=lambda: func(5))
five.grid(row=2, column=1)
six = Button(root, text='6', padx=35, pady=15,command=lambda: func(6))
six.grid(row=2, column=2)
seven = Button(root, text='7', padx=35, pady=15,command=lambda: func(7))
seven.grid(row=3, column=0)
eight = Button(root, text='8', padx=35, pady=15,command=lambda: func(8))
eight.grid(row=3, column=1)
nine = Button(root, text='9', padx=35, pady=15,command=lambda: func(9))
nine.grid(row=3, column=2)

plus = Button(root, text='+', padx=34, pady=15,command=lambda: plus_func())
plus.grid(row=4, column=1)
minus = Button(root, text='-', padx=35, pady=15,command=lambda: func())
minus.grid(row=4, column=2)
equal = Button(root, text='=', padx=75.5, pady=15,command=lambda: equal_func())
equal.grid(row=5, column=1, columnspan=2)
clear = Button(root, text='Clear', padx=24, pady=15,command=lambda: clear_func())
clear.grid(row=5, column=0)
root.mainloop()
