import tkinter as tk
from tkinter import *

import gui

window = Tk()

window.geometry("1000x500")

window.configure(bg="pink")

window.title("orders")


def order(dish):
    btn = Button(window, text=dish, font=("Ariel", 10), bg="pink", height=1, width=50, command=lambda: btn.pack_forget())
    btn.pack()


window.mainloop()
