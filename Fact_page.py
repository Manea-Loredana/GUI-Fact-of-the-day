import time
import tkinter as tk
import re
from time import strftime
import requests
from Scripts.bottle import app

HEIGHT = 600
WIDTH = 700

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame0 = tk.Frame(root, bg='#80c1ff', bd=5)
frame0.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.5, anchor='n')

label = tk.Label(frame0, text="Choose category", font='Helvetica 15')
label.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.5, anchor='n')
frame1 = tk.Frame(root, bg='#DFC8F2', bd=10)
frame1.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.1, anchor='n')

button8 = tk.Button(frame, height=4, width=15, bg='#fdb9e0', text="WIKIPEDIA")
button8.grid(row=0, column=2, padx=25, pady=25)

button2 = tk.Button(frame, height=4, width=15, bg='#fdb9e0', text="DOGS")
button2.grid(row=0, column=3, padx=25, pady=25)

button3 = tk.Button(frame, height=4, width=15, bg='#fdb9e0', text="ANIMALS")
button3.grid(row=0, column=4, padx=25, pady=25)

button5 = tk.Button(frame, height=4, width=15, bg='#cd9de2', text="ANIMATION")
button5.grid(row=1, column=2, padx=25, pady=25)

button6 = tk.Button(frame, height=4, width=15, bg='#cd9de2', text="FRUITS")
button6.grid(row=1, column=3, padx=25, pady=25)

button7 = tk.Button(frame, height=4, width=15, bg='#cd9de2', text="CARS")
button7.grid(row=1, column=4, padx=25, pady=25)

menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='Setting', menu=filemenu)
filemenu.add_command(label='Change domain')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = tk.Menu(menu)


# def createNewWindow():
#     # newWindow = tk.Toplevel(app)
#     # labelExample = tk.Label(newWindow, text="New Window")
#     # buttonExample = tk.Button(newWindow, text="New Window button")
#     #
#     # labelExample.pack()
#     # buttonExample.pack()


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


button = tk.Button(frame1, height=2, width=20, text='Continua', command=hide)
button.grid(row=0, column=0, padx=50, pady=1)
button1 = tk.Button(frame1, height=2, width=20, text='Stop', command=close)
button1.grid(row=0, column=8, padx=25, pady=1)

root.mainloop()
