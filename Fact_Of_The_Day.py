import tkinter as tk
import time
import re
from time import strftime
import requests
import random
import urllib.request
import io
import requests, json
from PIL import Image, ImageTk

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


def hide2():
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

for line in eventLines:
    randomLine = random.choice(eventLines)


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
text = "\n" + json_response['text'] + "\n"


# def show_cats_fact():
#     w = tk.Label(app, text=text)
#     w.pack()
#
#     def clicked():
#         r = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2')
#         json_response = r.json()[0]
#         text = json_response['text']
#         w.config(text=text)
#         btn = tk.Button(app, text='Next', command=clicked)
#         btn.pack()


# frame manager..........................................................
# ........................................................................................................................
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
        self.frames["Page3"] = Page3(parent=container, controller=self)
        self.frames["Page4"] = Page4(parent=container, controller=self)
        self.frames["Page5"] = Page5(parent=container, controller=self)
        self.frames["Page6"] = Page6(parent=container, controller=self)

        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageOne"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageTwo"].grid(row=0, column=0, sticky="nsew")
        self.frames["Page3"].grid(row=0, column=0, sticky="nsew")
        self.frames["Page4"].grid(row=0, column=0, sticky="nsew")
        self.frames["Page5"].grid(row=0, column=0, sticky="nsew")
        self.frames["Page6"].grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


# Start page/Principal page
# ...............................................................................................
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

        button8 = tk.Button(frame4, height=4, width=15, bg='#fdb9e0', text="History",
                            command=lambda: controller.show_frame("PageTwo"))
        button8.grid(row=0, column=2, padx=25, pady=25)

        button2 = tk.Button(frame4, height=4, width=15, bg='#fdb9e0', text="Cats",
                            command=lambda: controller.show_frame("PageOne"))
        button2.grid(row=0, column=3, padx=25, pady=25)

        button3 = tk.Button(frame4, height=4, width=15, bg='#fdb9e0', text="Astronomy",
                            command=lambda: controller.show_frame("Page3"))
        button3.grid(row=0, column=4, padx=25, pady=25)

        button5 = tk.Button(frame4, height=4, width=15, bg='#cd9de2', text="Fun",
                            command=lambda: controller.show_frame("Page4"))
        button5.grid(row=1, column=2, padx=25, pady=25)

        button6 = tk.Button(frame4, height=4, width=15, bg='#cd9de2', text="FRUITS",
                            command=lambda: controller.show_frame("Page5"))
        button6.grid(row=1, column=3, padx=25, pady=25)

        button7 = tk.Button(frame4, height=4, width=15, bg='#cd9de2', text="CARS",
                            command=lambda: controller.show_frame("Page6"))
        button7.grid(row=1, column=4, padx=25, pady=25)

        button1 = tk.Button(frame5, height=2, width=20, text='Close', command=close)
        button1.grid(row=0, column=4, padx=50, pady=25)
        button9 = tk.Button(frame5, height=2, width=20, text='Continue', command=hide)
        button9.grid(row=0, column=5, padx=25, pady=25)

        self._canvas.pack()


# Fact about  cats
# ...............................................................................................................
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        frame7 = tk.Frame(self, bg='#80c1ff', bd=5)
        frame7.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.5, anchor='n')

        frame25 = tk.Frame(frame7, bg='#80c1ff', bd=5)
        frame25.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor='n')
        frame6 = tk.Frame(self, bg='#80c1ff', bd=5)
        frame6.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.5, anchor='n')
        label = tk.Label(self, text="Cats facts", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(frame6, height=2, width=20, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=0, column=9, padx=10, pady=1)
        # button1 = tk.Button(frame6, height=2, width=20, text='Next', command=hide)
        # button1.grid(row=0, column=8, padx=25, pady=1)

        # get info about cats
        r = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2')
        json_response = r.json()[0]
        text = "\n" + json_response['text'] + "\n"
        # a gui for show info
        T1 = tk.Text(frame7, height=5, width=52)
        T1.pack()
        T1.insert(tk.END, text)

        catURL = 'http://aws.random.cat/meow'

        imageURL = json.loads(requests.get(catURL).content)["file"]

        class WebImage:
            def __init__(self, url):
                with urllib.request.urlopen(url) as u:
                    raw_data = u.read()
                # self.image = tk.PhotoImage(data=base64.encodebytes(raw_data))
                image = Image.open(io.BytesIO(raw_data))
                self.image = ImageTk.PhotoImage(image)

            def get(self):
                return self.image

        img = WebImage(imageURL).get()
        panel = tk.Label(frame25, image=img)
        panel.pack(side="bottom", fill="both", expand="no")

        def clicked():
            r = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2')
            json_response = r.json()[0]
            text1 = json_response['text']
            T1.delete("1.0", "end")  # if you want to remove the old data
            T1.insert(tk.END, text1)

        # btn = tk.Button(frame6, height=2, width=20, text='Next', command=clicked)
        # btn.grid(row=0, column=8, padx=10, pady=1)
        button_Close = tk.Button(frame6, height=2, width=20, text='Close', command=close)
        button_Close.grid(row=0, column=10, padx=10, pady=1)


# Fact from wiki / event that happen the curent day
# ...................................................................................................................


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="A random event that happen today", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        frame8 = tk.Frame(self, bg='#80c1ff', bd=5)
        frame8.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.5, anchor='n')
        frame9 = tk.Frame(self, bg='#80c1ff', bd=5)
        frame9.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.5, anchor='n')

        T = tk.Text(frame8, height=5, width=52)
        l = tk.Label(frame8, text="Fact of the Day")
        l.config(font=("Courier", 14))

        Fact = ("A random event from this day in history On" + strftime("%B %d, ") + randomLine)

        # Create button for next text.

        l.pack()
        T.pack()
        # Insert The Fact.
        T.insert(tk.END, Fact)

        def clicked1():
            T.delete("1.0", "end")  # if you want to remove the old data
            Fact2 = ("A random event from this day in history On" + strftime("%B %d, ") + randomLine)
            T.insert(tk.END, Fact2)

        #
        # btn1 = tk.Button(frame9, height=2, width=20, text='Next', command=clicked1())
        # btn1.grid(row=0, column=9, padx=10, pady=1)
        button_Close1 = tk.Button(frame9, height=2, width=20, text='Close', command=close)
        button_Close1.grid(row=0, column=11, padx=10, pady=1)
        buttonStart = tk.Button(frame9, height=2, width=20, text="Go to the start page",
                                command=lambda: controller.show_frame("StartPage"))
        buttonStart.grid(row=0, column=10, padx=10, pady=1)


# ...................................................................
class Page3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Astronomy Facts", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        frame10 = tk.Frame(self, bg='#80c1ff', bd=5)
        frame10.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.5, anchor='n')
        frame11 = tk.Frame(self, bg='#80c1ff', bd=5)
        frame11.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.5, anchor='n')

        btn2 = tk.Button(frame11, height=2, width=20, text='Next')
        btn2.grid(row=0, column=9, padx=10, pady=1)
        button_Close3 = tk.Button(frame11, height=2, width=20, text='Close', command=close)
        button_Close3.grid(row=0, column=11, padx=10, pady=1)
        buttonStart1 = tk.Button(frame11, height=2, width=20, text="Go to the start page",
                                 command=lambda: controller.show_frame("StartPage"))
        buttonStart1.grid(row=0, column=10, padx=10, pady=1)


# Random fun facts
# .................................................................................................
class Page4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Random Fun Facts", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        frame12 = tk.Frame(self, bg='#80c1ff', bd=5)
        frame12.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.5, anchor='n')
        frame13 = tk.Frame(self, bg='#80c1ff', bd=5)
        frame13.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.5, anchor='n')

        url = "https://uselessfacts.jsph.pl/random.json?language=en"
        response = requests.request("GET", url)
        data = json.loads(response.text)
        text5 = "\n" + data['text'] + "\n"
        # a gui for show info
        T3 = tk.Text(frame12, height=5, width=52)
        T3.pack()
        T3.insert(tk.END, text5)

        def clicked3():
            url2 = "https://uselessfacts.jsph.pl/random.json?language=en"
            response2 = requests.request("GET", url2)
            data2 = json.loads(response2.text)
            text6 = "\n" + data2['text'] + "\n"
            # a gui for show info
            T3.delete("1.0", "end")  # if you want to remove the old data
            T3.insert(tk.END, text6)

        # btn3 = tk.Button(frame13, height=2, width=20, text='Next', command=clicked3())
        # btn3.grid(row=0, column=9, padx=10, pady=1)
        button_Close4 = tk.Button(frame13, height=2, width=20, text='Close', command=close)
        button_Close4.grid(row=0, column=13, padx=10, pady=1)
        buttonStart2 = tk.Button(frame13, height=2, width=20, text="Go to the start page",
                                 command=lambda: controller.show_frame("StartPage"))
        buttonStart2.grid(row=0, column=10, padx=10, pady=1)


# ...........................................................................................................................
class Page5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        frame14 = tk.Frame(self, bg='#80c1ff', bd=5)
        frame14.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.5, anchor='n')
        frame15 = tk.Frame(self, bg='#80c1ff', bd=5)
        frame15.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.5, anchor='n')

        button100 = tk.Button(frame15, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))

        button100.grid(row=0, column=9, padx=10, pady=1)
        button_Close33 = tk.Button(frame15, height=2, width=20, text='Close', command=close)
        button_Close33.grid(row=0, column=10, padx=10, pady=1)


# ...................................................................................................................
class Page6(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        frame16 = tk.Frame(self, bg='#80c1ff', bd=5)
        frame16.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.5, anchor='n')
        frame17 = tk.Frame(self, bg='#80c1ff', bd=5)
        frame17.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.5, anchor='n')
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))

        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
