import tkinter as tk
from tkinter import *

# to get the name of the restaurant run, the func- get_text_from_name_file()
# to get the adress of the restaurant, run the func - get_text_from_adress_file()
# to get the list of dishes, run the func- get_list_of_dishes()
def create_window(text):
    window = Tk()
    window.title(text)
    window.configure(width=1000, height=500)
    window.configure(bg='pink')
    return window


rest_reg = create_window("Restaurant Registration")


# when the restaurant finishes
# adding dishes it clears the text box
def clear():
    take_dishes.delete(1.0, END)


# grabs the text from the text box
def get_text():
    print(take_dishes.get(1.0, END))


# creates a text file with the dishes the restaurant had typed
def create_dish_file():
    dishes_file = open("dishes_file.txt", "w+")
    with open('dishes_file.txt', 'w') as dishes_file:
        dishes_file.write(take_dishes.get(1.0, END))
    dishes_file.close()


def create_restaurantName_file():
    name_file = open("restaurantName.txt", "w+")
    with open('restaurantName.txt', 'w') as dishes_file:
        name_file.write(take_name.get(1.0, END))
    name_file.close()


def create_adress_file():
    adress = open("adress.txt", "w+")
    with open('adress.txt', 'w') as adress:
        adress.write(take_adress.get(1.0, END))
    adress.close()


# gets a list that contains what the text file contains
def get_text_from_dish_file():
    f = open("dishes_file.txt")
    lines = f.readlines()
    return lines


def get_text_from_name_file():
    f = open("restaurantName.txt")
    lines = f.readlines()
    lines = lines[0].strip()
    return lines


def get_text_from_adress_file():
    f = open("adress.txt")
    lines = f.readlines()
    lines = lines[0].strip()
    return lines


def create_text_label(text):
    name = Label(rest_reg, text=text, bg="pink")
    name.config(font=("David", 14))
    name.pack()


create_text_label("Enter the name of the restaurant:")

take_name = Text(rest_reg, width=20, height=3, font=("David", 14))
take_name.pack(pady=10)


def get_name_button():
    getName_button_frame = Frame(rest_reg)
    getName_button_frame.pack()
    get_name_button = Button(getName_button_frame, text="Get Name", command=create_restaurantName_file)
    get_name_button.pack()


get_name_button()

create_text_label("Enter the adress of the restaurant:")
take_adress = Text(rest_reg, width=20, height=3, font=("David", 14))
take_adress.pack(pady=15)


def get_adress_button():
    getAdress_button_frame = Frame(rest_reg)
    getAdress_button_frame.pack()

    get_adress_button = Button(getAdress_button_frame, text="Get Adress", command=create_adress_file)
    get_adress_button.pack()


get_adress_button()

create_text_label("Enter the available dishes with '_' in between :")

take_dishes = Text(rest_reg, width=40, height=10, font=("David", 14))
take_dishes.pack(pady=20)


def finish_button():
    finish_button_frame = Frame(rest_reg)
    finish_button_frame.pack()

    finish_button = Button(finish_button_frame, text="Finish", command=rest_reg.destroy)
    finish_button.grid(row=0, column=0)


def get_dishes_button():
    getTdishes_button_frame = Frame(rest_reg)
    getTdishes_button_frame.pack()

    get_text_button = Button(getTdishes_button_frame, text="Insert Dishes", command=create_dish_file)
    get_text_button.pack()


get_dishes_button()
finish_button()

rest_reg.mainloop()


# separates the file with "_"
def get_list_of_dishes():
    dish_list = get_text_from_dish_file()
    dish_list = dish_list[0].strip()
    dish_list = dish_list.split("_")
    return dish_list


# print(get_text_from_name_file())
# print(get_text_from_adress_file())
# get_list_of_dishes()

# returns a list of the restaurant deatails-
# 1 - name
# 2 - adress
# 3 - dish list
def get_details_about_the_restaurant():
    return [get_text_from_name_file(), get_text_from_adress_file(), get_list_of_dishes()]


print(get_details_about_the_restaurant())



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
