import random
import time
from tkinter import *
from tkinter import PhotoImage


def bros():
    x = random.choice(['1.png', '2.png', '3.png',
                       '4.png', '5.png', '6.png'])
    return x


def img(event):
    global j1, j2
    for i in range(10):
        j1: PhotoImage = PhotoImage(file=(bros()))
        j2 = PhotoImage(file=(bros()))
        lab1['image'] = j1
        lab2['image'] = j2
        root.update()
        time.sleep(0.05)


root = Tk()
root.geometry('1000x500')
root.title('Play dice!')
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file='5.png'))

font = PhotoImage(file='fon.png')
Label(root, image=font).pack()

lab1 = Label(root)
lab1.place(relx=0.28, rely=0.5, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.72, rely=0.5, anchor=CENTER)

root.bind('<1>', img)
img('event')

root.mainloop()
