import tkinter as tk
from tkinter import *


def click(chosen_item):
    return chosen_item


item_list = ["1", "2", "3"]


def choose_from(item_list):
    window = Tk()

    window.geometry("1000x500")

    window.title("choose restaurat")

    for item in item_list:
        b = Button(window, text=item, font=("Ariel", 10), height=1, width=1000, command=lambda: click(item))
        b.pack()
    finish_frame = Frame(window)
    finish_frame.pack()
    btn = Button(finish_frame, text="finish", font=("Ariel", 10), height=1, width=10, command=window.destroy)
    btn.pack()
    window.mainloop()


choose_from(item_list)



