# import tkinter
# top = tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()
import time
print('creation time: ',time.asctime())
to_do_list = {}
command_list = ['show my tasks','add a task']
while True:
    answer = input('Type "Show my tasks" to show your current to-do list\nType "Add a task" to add something to your to-do list\n').lower()
    if answer == 'show my tasks':
        print(*to_do_list,sep="\n")
    if answer == 'add a task':
        to_do_list[input('Type a task you want: ')] = (time.asctime())
    if answer not in command_list:
        print('Please write correct command')
