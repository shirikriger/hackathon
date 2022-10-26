import tkinter as tk
from tkinter import *

rest = ""
dish = ""
name = ""
running = True


def get_text_from_name_file():
    f = open("name.txt")
    lines = f.readlines()
    lines = lines[0].strip()
    return lines


def get_restaurant(rest_list):
    window = Tk()

    window.geometry("1000x500")

    window.title("choose restaurat")

    def should_stop(rest_name):
        global rest
        global running
        running = False
        rest = rest_name
        window.destroy()

    def button_create(resta):
        b = Button(window, text=resta, font=("Ariel", 10), height=1, width=1000, command=lambda: should_stop(resta))
        b.pack()

    while running:
        for item in rest_list:
            button_create(item)
        window.mainloop()
        return rest


def get_dish(dish_list):
    window = Tk()

    window.geometry("1000x500")

    window.title("choose restaurat")

    take_name = Text(window, width=20, height=3, font=("David", 14))
    take_name.pack()
    name_file = open("name.txt", "w+")
    with open("name.txt", "w") as name_file:
        name_file.write(take_name.get(1.0), END)
    name_file.close()

    def should_stop(dish_name):
        global dish
        global running
        global name
        running = False
        dish = dish_name
        name = get_text_from_name_file()
        window.destroy()

    def button_create(resta):
        b = Button(window, text=resta, font=("Ariel", 10), height=1, width=1000, command=lambda: should_stop(resta))
        b.pack()

    while running:
        for item in dish_list:
            button_create(item)
        window.mainloop()
        return dish, name
