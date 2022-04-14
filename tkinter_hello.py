from tkinter import *


def say_hi():
    print("Hi there, Everyone ")


class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit())
        self.button.pack(side=LEFT)
        self.hi_there = Button(frame, text="Hello", fg="green", command=say_hi)
        self.hi_there.pack(side=LEFT)
