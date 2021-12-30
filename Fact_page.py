import time
import tkinter as tk

root = tk.Tk()
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='Setting', menu=filemenu)
filemenu.add_command(label='Chose domain')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = tk.Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')


def close():
    root.destroy()


def show():
    root.deiconify()


def hide():
    root.withdraw()
    time.sleep(5)
    show()


button = tk.Button(text='Continua', command=hide)
button.pack()
button1 = tk.Button(text='Stop', command=close)
button1.pack()

root.mainloop()
