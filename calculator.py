from tkinter import *

root = Tk()
root.title('Calculator')
root.iconphoto(False, PhotoImage(file='C:/Users/Litefallen/PycharmProjects/Calculator/Custom.gif'))  # the only
# working way to add an icon without pain in a** in tkinter

entry = Entry(root, width=42)
entry.grid(row=0, column=0, columnspan=3, pady=10)
result = 0
prev_function = None
math_operations_list = ['plus', 'minus', 'multiply', 'divide']


def action_func(do):  # get entry
    arg1 = entry.get()
    entry.delete(0, END)

    def math_func(action, arg):
        global result
        if not prev_function:
            result += int(arg)
        if action == 'show result':
            if prev_function == 'minus':
                result -= int(arg)
                entry.insert(0, str(result))
            if prev_function == 'plus':
                result += int(arg)
                entry.insert(0, str(result))
            result = 0
        if action == 'clear':
            result = 0
            entry.delete(0, END)

    math_func(do, arg1)
    global prev_function
    if do in math_operations_list:
        prev_function = do
    else:
        prev_function = None


def push_nums(x):
    line = entry.get()
    entry.delete(0, END)
    entry.insert(0, line + str(x))


zero = Button(root, text='0', padx=35, pady=15, command=lambda: push_nums(0))
zero.grid(row=4, column=0)
one = Button(root, text='1', padx=35, pady=15, command=lambda: push_nums(1))
one.grid(row=1, column=0)
two = Button(root, text='2', padx=35, pady=15, command=lambda: push_nums(2))
two.grid(row=1, column=1)
three = Button(root, text='3', padx=35, pady=15, command=lambda: push_nums(3))
three.grid(row=1, column=2)
four = Button(root, text='4', padx=35, pady=15, command=lambda: push_nums(4))
four.grid(row=2, column=0)
five = Button(root, text='5', padx=35, pady=15, command=lambda: push_nums(5))
five.grid(row=2, column=1)
six = Button(root, text='6', padx=35, pady=15, command=lambda: push_nums(6))
six.grid(row=2, column=2)
seven = Button(root, text='7', padx=35, pady=15, command=lambda: push_nums(7))
seven.grid(row=3, column=0)
eight = Button(root, text='8', padx=35, pady=15, command=lambda: push_nums(8))
eight.grid(row=3, column=1)
nine = Button(root, text='9', padx=35, pady=15, command=lambda: push_nums(9))
nine.grid(row=3, column=2)
plus = Button(root, text='+', padx=34, pady=15, command=lambda: action_func('plus'))
plus.grid(row=4, column=1)
minus = Button(root, text='-', padx=35, pady=15, command=lambda: action_func('minus'))
minus.grid(row=4, column=2)
equal = Button(root, text='=', padx=75.5, pady=15, command=lambda: action_func('show result'))
equal.grid(row=5, column=1, columnspan=2)
clear = Button(root, text='Clear', padx=24, pady=15, command=lambda: action_func('clear'))
clear.grid(row=5, column=0)
root.mainloop()
