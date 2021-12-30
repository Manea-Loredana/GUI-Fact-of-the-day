

import time
import tkinter as tk

root = tk.Tk()


def close():
    root.destroy()


def show():
    root.deiconify()


def hide():
    root.withdraw()
    time.sleep(5)
    show()


tk.Frame(root, width=250, height=100).pack()
button = tk.Button(text='Continua', command=hide)
button.pack()
button1 = tk.Button(text='Stop', command=close)
button1.pack()

root.mainloop()
