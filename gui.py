import tkinter as tk
from tkinter import *


def click(chosen_item):
    return chosen_item


def get_text_from_name_file():
    f = open("name.txt")
    lines = f.readlines()
    lines = lines[0].strip()
    return lines


def get_restaurant(rest_list):
    window = Tk()

    window.geometry("1000x500")

    window.title("choose restaurat")
    take_name = Text(window, width=20, height=3, font=("David", 14))
    take_name.pack()
    name_file = open("name.txt", "w+")
    with open("name.txt", "w") as name_file:
        name_file.write(take_name.get(1.0), END)
    name_file.close()
    for item in rest_list:
        b = Button(window, text=item, font=("Ariel", 10), height=1, width=1000, command=lambda: click(item))
        b.pack()
    finish_frame = Frame(window)
    finish_frame.pack()
    btn = Button(finish_frame, text="finish", font=("Ariel", 10), height=1, width=10, command=window.destroy)
    btn.pack()
    window.mainloop()


def get_dish(dish_list):
    window = Tk()

    window.geometry("1000x500")

    window.title("choose restaurat")

    for item in dish_list:
        b = Button(window, text=item, font=("Ariel", 10), height=1, width=1000, command=lambda: click(item))
        b.pack()
    finish_frame = Frame(window)
    finish_frame.pack()
    btn = Button(finish_frame, text="finish", font=("Ariel", 10), height=1, width=10, command=window.destroy)
    btn.pack()
    window.mainloop()
