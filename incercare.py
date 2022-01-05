import tkinter as tk
import time
import re
from time import strftime
import requests
from tkinter import ttk
import random

TITLE_FONT = ("Helvetica", 18, "bold")


# define function........................................................

def close():
    app.destroy()


def show():
    app.deiconify()


def hide():
    app.withdraw()
    time.sleep(5)
    show()


# WIKIPEDIA FACT ...............................................


def month_and_day(asString=True):
    if asString:
        return strftime("%B_%d")
    return strftime("%m_%d")


def extractLines(rawtext):
    rawlist = rawtext.split('\n')
    eventlist = []
    eventswitch = False
    for curline in rawlist:
        # Only extract Birthdays and Events.
        if 'id="Events"' in curline:
            eventswitch = True
        if 'id="Births"' in curline:
            eventswitch = False
        if eventswitch:
            eventlist.append(curline)

    # This code will help clean up some of the wikipedia formatting
    startrecord = False
    parsedlist = []
    for curline in eventlist:
        if '<li>' in curline:
            startrecord = True
        if startrecord:
            modline = curline.replace('<li>', '')
            modline = modline.replace('</li>', '')
            modline = modline.replace('<lu>', '')
            modline = modline.replace('</lu>', '')
            modline = modline.replace('<ul>', '')
            modline = modline.replace('</ul>', '')
            modline = modline.replace('</a>', '')
            modline = modline.replace('<a *>', '')
            modline = modline.replace('<i>', '')
            modline = modline.replace('</i>', '')
            modline = modline.replace('<u>', '')
            modline = modline.replace('</u>', '')
            modline = modline.replace('&#8211; ', '')
            subbed = re.sub('<a.*?>', '', modline)
            parsedlist.append(subbed)
        if '</li>' in curline:
            startrecord = False

    return parsedlist


urlToGet = 'https://simple.wikipedia.org/wiki/' + month_and_day(True)
request = requests.get(urlToGet)
eventLines = extractLines(request.text)
# fEvents = open('EventsOfToday.txt', 'w')
fEvents = open('EventsOfToday.txt', "w", encoding="utf-8")

# Write all facts out to a file.


for line in eventLines:
    fEvents.write(line + '\n')

randomLine = random.choice(eventLines)
print("A random event from this day in history...")
print("On " + strftime("%B %d, ") + randomLine)
print("Done")


def show_wiki_fact(self):
    T = tk.Text(self, height=5, width=52)
    l = tk.Label(self, text="Fact of the Day")
    l.config(font=("Courier", 14))

    Fact = ("A random event from this day in history On" + strftime("%B %d, ") + randomLine)

    # Create button for next text.

    b1 = tk.Button(self, text="Next")

    # Create an Exit button.
    b2 = tk.Button(self, text="Exit",
                   command=app.destroy)
    l.pack()
    T.pack()
    b2.pack()
    # Insert The Fact.
    T.insert(tk.END, Fact)


# ...............................................................................
# Cats facts .........................................................................
r = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2')
json_response = r.json()[0]
text = json_response['text']


def show_cats_fact():
    w = tk.Label(app, text=text)
    w.pack()

    def clicked():
        r = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2')
        json_response = r.json()[0]
        text = json_response['text']
        w.config(text=text)
        btn = tk.Button(app, text='Next', command=clicked)
        btn.pack()


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.frames["StartPage"] = StartPage(parent=container, controller=self)
        self.frames["PageOne"] = PageOne(parent=container, controller=self)
        self.frames["PageTwo"] = PageTwo(parent=container, controller=self)

        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageOne"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageTwo"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self._canvas = tk.Canvas(self, bg='white', width=700, height=400)
        self.background_image = tk.PhotoImage(file='landscape.png')
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)
        frame4 = tk.Frame(self, bg='#80c1ff', bd=5)
        frame4.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.5, anchor='n')
        frame5 = tk.Frame(self, bg='#80c1ff', bd=5)
        frame5.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.5, anchor='n')

        label = tk.Label(self, text="Choose category", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button8 = tk.Button(frame4, height=4, width=15, bg='#fdb9e0', text="WIKIPEDIA",
                            command=lambda: controller.show_frame("PageOne"))
        button8.grid(row=0, column=2, padx=25, pady=25)

        button2 = tk.Button(frame4, height=4, width=15, bg='#fdb9e0', text="Cats",
                            command=lambda: controller.show_frame("PageOne"))
        button2.grid(row=0, column=3, padx=25, pady=25)

        button3 = tk.Button(frame4, height=4, width=15, bg='#fdb9e0', text="ANIMALS",
                            command=lambda: controller.show_frame("PageOne"))
        button3.grid(row=0, column=4, padx=25, pady=25)

        button5 = tk.Button(frame4, height=4, width=15, bg='#cd9de2', text="ANIMATION",
                            command=lambda: controller.show_frame("PageOne"))
        button5.grid(row=1, column=2, padx=25, pady=25)

        button6 = tk.Button(frame4, height=4, width=15, bg='#cd9de2', text="FRUITS",
                            command=lambda: controller.show_frame("PageOne"))
        button6.grid(row=1, column=3, padx=25, pady=25)

        button7 = tk.Button(frame4, height=4, width=15, bg='#cd9de2', text="CARS",
                            command=lambda: controller.show_frame("PageOne"))
        button7.grid(row=1, column=4, padx=25, pady=25)

        button1 = tk.Button(frame5, height=2, width=20, text='Close', command=close)
        button1.pack()

        self._canvas.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        frame7 = tk.Frame(self, bg='#80c1ff', bd=5)
        frame7.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.5, anchor='n')
        frame6 = tk.Frame(self, bg='#80c1ff', bd=5)
        frame6.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.5, anchor='n')
        label = tk.Label(self, text="This is page 1", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(frame6, height=2, width=20, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=0, column=9, padx=25, pady=1)
        # button1 = tk.Button(frame6, height=2, width=20, text='Next', command=hide)
        # button1.grid(row=0, column=8, padx=25, pady=1)

        # get info about cats
        r = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2')
        json_response = r.json()[0]
        text = json_response['text']
        # a gui for show info
        w = tk.Label(frame7, text=text)
        w.pack()

        def clicked():
            app.withdraw()
            time.sleep(5)
            r = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2')
            json_response = r.json()[0]
            text = json_response['text']
            w.config(text=text)
            show()

        btn =tk.Button(frame6, text='Next', command=clicked)
        btn.grid(row=0, column=8, padx=25, pady=1)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))

        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
