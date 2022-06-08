# def get_full_name(employee: dict):
#     return f'{employee["first_name"]} {employee["last_name"]}'
#
#
# def create_employee(first_name, last_name, get_full_name_func):
#     d = {
#         "first_name": first_name,
#         "last_name": last_name,
#         "get_full_name": get_full_name_func
#     }
#     return d
#
#
# d = create_employee("Vytautas", "Sluckas", get_full_name)
#
# print(d)
# print(d["get_full_name"](d))

# my_list = [1,2,3,4,5]
#
# new_list = []
# for number in my_list:
#     if number % 2 == 0:
#         new_list.append(number)
#
#
# print(new_list)
#
my_list = [4, 3, 2, 1]
# my_list2 = []
#
# for number in my_list:
#     my_list2.append(number ** 2)
# #
# print(my_list2)
#
# def square(x):
#     return x**2
#
# my_list3 = map(square, my_list)
#
# print(str(my_list3))
# #
# #
# numbers = "4, 3, 2, 1"
#
# p, a, t, k = map(float, numbers.split(","))
#
# print(p, a, t, k)
#
# my_list = [4, 3, 2, 1]
#
#
# def more_than_two(some_list: list) -> list:
#     second_list = []
#     for number in some_list:
#         if number > 2:
#             second_list.append(number)
#     return second_list
#
# print(more_than_two(my_list))
#
# def more_than_two(x):
#     return x > 2
#
# new_list = filter(more_than_two, my_list)
# print(list(new_list))
#
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
#
# new_list = filter(lambda x: x % 2)
#
# my_list = [1, 2, 3, 4]
#
# print(sum(my_list))
# print(min(my_list))
# print(max(my_list))
#
# from statistics import mean, median
#
# print(mean(my_list))
# print(median(my_list))
#
# my_list = [10, 15, 26, 87]
#
# new_list = [number**2 for number in my_list]
#
# print(new_list)
#
#
# my_string = "Labas vakaras. Kaip tu. Viso gero"
#
# new_string = my_string.split(". ")
#
# print(new_string)
#
# new_string2 = map(lambda x: x+"!", new_string)
#
# print(list(new_string2))
#
#
# my_string = "Labas vakaras. Kaip tu. Viso gero"
#
# my_string = my_string.split(".")
#
# new_string = [sentence + "!" for sentence in my_string]
#
# print(new_string)
#
#
# new_list = list(range(50))
#
# my_list = [item * 10 for item in new_list]
#
# print(my_list)
#
# new_list2 = [item for item in new_list if item % 7 == 0]
# new_list3 = [item ** 2 for item in new_list]
#
#
# print(new_list3)
# print(new_list2)
#
# from statistics import mean, median
#
#
# print(sum(new_list3))
# print(min(new_list3))
# print(max(new_list3))
# print(mean(new_list3))
# print(median(new_list3))
# new_list3.sort(reverse=True)
# print(new_list3)
# first_list = ['gaidis', 1, 17.14, 0, 'miznius']
#
# new_list2 = [x for x in first_list if type(x) == int or type(x) == float]
#
# print(new_list2)
#
# def sum_list(numbers_list: list[float]) -> float:
#     y = 0
#     for x in numbers_list:
#         y = y + x
#     print(y)
#
# skaiciu_sarasas = [14, 15.6, 17.8]
#
# sum_list(skaiciu_sarasas)

# sarasas = [1, 2, 3]
# print(len(sarasas))
# #

#
#
#
# def check_id(id:str) -> bool:
#
#     if len(id)!=11:
#         return False
#
#     for i in id:
#         try:
#             int(i)
#         except Exception as e:
#             return False
#
#     if(
#             3 <= int(id[0]) and int(id[0]) <= 6 and
#         int(id[3]) == 0 and int(id[3]) == 1):
#         return True
#
#
#     else:
#         return False
#
#
# print(check_id("39619043712"))
#
# # #
#

#
# class Workers:
#     def __init__(self, name, surname, wage):
#         self.name = name
#         self.surname = surname
#         self.__wage = wage
#
#     @property
#     def wage(self) -> int:
#         return self.__wage

    # @wage_after.setter
    # def wage_after(self. new: int) -> int:
    #     self.__wage = new
#
#
# antanas = Workers('Antanas', 'Antaniukas', 650)
#
# print(antanas.wage)
#
# antanas.__wage = -150
#
# print(antanas.__wage)
#
#
# class House:
#     def __init__(self, size: str, value: int):
#         self.size = size
#         self.__value = value
#
#     @property
#     def value(self) -> int:
#         return self.__value
#
#     @value.setter
#     def value(self, new: int) -> None:
#         if new < 0:
#             print('Value cant be negative!!!')
#         else:
#             self.__value = new
#
#
# house1 = House('hugeee', 285000)
#
# print(house1.value)
#
# house1.value = -200
#
# print(house1.value)










#
# class Car:
#     def __init__(self, year: int, model: str, fuel_type: str):
#         self.year = year
#         self.model = model
#         self.fuel_type = fuel_type
#         print(f'Made year is: {self.year}, the model is: {self.model}, fuel type is: {self.fuel_type}')
#
#     def driving(self):
#         print('Driving!!')
#
#     def stadning_still(self):
#         print('Standing still!!')
#
#     def refueling(self):
#         print('Refueling!')
#
#
# class Electric(Car):
#
#     def refueling(self):
#         print('Baterry charged')
#
#     def drive_autonomous(self):
#         print('Driving autonomous!')
#
#
# bmw1 = Car(2008, 'e60', 'diesel')
#
# bmw2 = Electric(2020, 'Tesla model3', 'Electric')
#
# bmw2.refueling()
#
#
#








#
#
#
# import datetime
#
#
# class Worker:
#     def __init__(self, name: str, hourly_salary: float, working_from: str):
#         self.name = name
#         self.hourly_salary = hourly_salary
#         self.working_from = working_from
#
#     def worked_days(self) -> int:
#         now = datetime.datetime.now()
#         data = datetime.datetime.strptime(self.working_from, "%Y-%m-%d")
#         worked_time = now - data
#         return worked_time.days
#
#     def salary_from(self) -> float:
#         data = self.worked_days()
#         salary = int(data.days) * self.hourly_salary * 8
#         return salary
#
#
# class NormalWorker(Worker):
#
#     def salary_from(self) -> float:
#         data = self.worked_days()
#         woking_days = data - ((data / 7) * 2)
#         salary = woking_days * self.hourly_salary * 8
#         return salary
#
#     def prisistatymas(self):
#         return (f'Mano vardas yra {self.name}, as pradejau dirbti {self.working_from}, iki siandienos as uzdirbau {self.salary_from()} euru')
#
#
# worker1 = Worker('Antaniukas', 3.2, "2022-02-02")
# worker2 = NormalWorker('VladimirVladimirovic', 1.8, "2022-01-23")
# worker3 = NormalWorker('TomasLingvinis', 7, '2022-02-03')
#
#
# print(worker2.prisistatymas())
# print(worker3.prisistatymas())

#
#
#
# from random import randint
# class Workers:
#
#     def __init__(self, name, surname, wage):
#         self.name = name
#         self.surname = surname
#         self.__wage = wage
#
#     def calc_average(self) -> int:
#         return self.__wage // 10
#
#     @property
#     def wage_after(self) -> int:
#         return self.__wage
#
#     @wage_after.setter
#     def wage_after(self) -> int:
#         return self.__wage
#
#
# class Company:
#
#     def __init__(self):
#         self.worker = Workers('Antanas','Antaniukas', 650)
#
#     def get_company_financials(self):
#         return self.worker.wage_after
#
#     def get_random_number(self, number: int) -> int:
#         try:
#             nr = randint(0, 100)
#             if type(number) != int:
#                 raise ValueError('Not the value I wanted')
#             return number - nr + self.get_company_financials()
#         except Exception:
#             pass
#
#
# my_company = Company()
# print(my_company.get_random_number(25))
#

#
# class Tree:
#     def __init__(self, name:str, location:str, height:int):
#         self.name = name
#         self.location = location
#         self.height = height
#
#     def im_green(self):
#         print('I`m very green and big ma boy')
#
#
#
# class BigTree(Tree):
#
#     def introduction(self):
#         print("My name is {self.name}. I live in {self.location} and my height is {self.height} meters.")
#
#
# tree1 = Tree('Oak', 'Lithuania', 17)
# tree2 = BigTree('Spruce', 'Norway', 12)
#
# tree2.introduction()

#
# from tkinter import Tk, Label
#
# window = Tk()
# window.title('Test')
# window.geometry("250x200")
# text = Label(window, text='This is random text')
# text.pack()
#
#
# window.mainloop()
#
#
# from tkinter import Tk, Frame, Button, BOTTOM, LEFT, Y
#
# window = Tk()
# window.geometry("450x250")
# top = Frame(window)
# bottom = Frame(window)
#
# button1 = Button(top, text='Button #1')
# button2 = Button(top, text='Button #2')
# button3 = Button(top, text='Button #3')
# button4 = Button(top, text='Button #4')
#
# top.pack()
# bottom.pack(side=BOTTOM)
#
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM, fill=Y)
#
# window.mainloop()
#

#
# from tkinter import *
#
# window = Tk()
# window.geometry("400x400")
#
# text1 = Label(window, text="Name")
# field1 = Entry(window)
# text2 = Label(window, text="Surname")
# field2 = Entry(window)
# check_button = Checkbutton(window, text="Place check")
#
# text1.grid(row=0, column=0, sticky=E)
# field1.grid(row=0, column=1)
# text2.grid(row=1, column=0, sticky=E)
# field2.grid(row=1, column=1)
# check_button.grid(row=2, columnspan=2)
#
# window.mainloop()
#
# from tkinter import *
# window = Tk()
# window.geometry("400x400")
#
# def print1(event):
#     print("left mouse button clicked!")
#
# def print2(event):
#     print("right mouse button clicked!")
#
# def print3(event):
#     print("ENTER pressed!")
#
# my_button = Button(window, text="Printing")
# my_button.bind("<Button-1>", print1)
# my_button.bind("<Button-3>", print2)
# window.bind("<Return>", print3)
# my_button.pack()
#
# window.mainloop()

#
#
# from tkinter import *
# window = Tk()
#
# def print1():
#     print("Printing!")
#
# my_button = Button(window, text="Printing", command=print1)
# window.bind("<Return>", lambda event: print1())
# my_button.pack()
#
# window.mainloop()
#

#
# from tkinter import *
#
# window = Tk()
#
# def print1():
#     inputeded = field1.get()
#     result["text"] = inputeded
#
#
# text1 = Label(window, text="Type your word")
# field1 = Entry(window)
# my_button = Button(window, text="Input", command=print1)
# result = Label(window, text="")
#
# text1.grid(row=0, column=0)
# field1.grid(row=0, column=1)
# my_button.grid(row=0, column=2)
# result.grid(row=1, columnspan=3)
#
# window.mainloop()

#
# from tkinter import *
#
# window1 = Tk()
# window1.geometry("400x400")
# box1 = Listbox(window1, width=40, height=40)
# list1 = range(123456789100, 123456789300)
# box1.insert(END, *list1)
# box1.pack(side=LEFT)
# window1.mainloop()
#
# from tkinter import *
#
# langas = Tk()
# sarasas = range(1, 200)
#
# def spausdinti():
#     pasirinkta = sarasas[boksas.curselection()[0]]
#     uzrasas["text"] = pasirinkta
#
# mygtukas = Button(langas, text="Spausdinti",
# command=spausdinti)
#
# uzrasas = Label(langas, text="Nieko")
# boksas = Listbox(langas, selectmode=SINGLE)
# boksas.insert(END, *sarasas)
# boksas.pack(side=LEFT)
# mygtukas.pack()
# uzrasas.pack()
# langas.mainloop()

#
#
# from tkinter import *
# langas = Tk()
#
# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 0)
#
# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")
# submeniu.add_command(label="Antras")
# langas.mainloop()
#
# from tkinter import *
# langas = Tk()
#
# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 0)
#
# def antras():
#     print("Antras!")
#
# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")
# submeniu.add_command(label="Antras",
# command=antras)
# langas.mainloop()

#
# from tkinter import *
# langas = Tk()
#
# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 0)
# submeniu2 = Menu(meniu, tearoff = 0)
# submeniu3 = Menu(meniu, tearoff = 0)
#
# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")
#
# submeniu.add_command(label="Antras")
# submeniu.add_separator()
# submeniu.add_command(label="Trečias")
#
#
# meniu.add_cascade(label="Meniu 2",
# menu=submeniu2)
# submeniu2.add_command(label="1")
# submeniu2.add_command(label="2")
#
# meniu.add_cascade(label="Meniu 3",
# menu=submeniu3)
#
# langas.mainloop()
#
#
# from tkinter import *
#
# window = Tk()
# window.geometry("400x400")

#
# def sumbit():
#     user_input = field1.get()
#     print(user_input)
#     result["text"] = f"Sveikas {user_input}"
#
#
# name = Label(window, text="Enter your name")
# button = Button(window, text="Enter", command=sumbit)
# field1 = Entry(window)
# result = Label(window, text="")
#
# name.pack()
# field1.pack()
# button.pack()
# result.pack()
#
#
# window.mainloop()



# from tkinter import *
# langas = Tk()
#
# status = Label(langas, text="Nieko nedaro...", bd=1, relief=SUNKEN, anchor=W)
# status.pack(side=BOTTOM, fill=X)
# langas.mainloop()

#
# from tkinter import *
# langas = Tk()
#
# def daryti():
#     status["text"] = "Dabar daro"
#
# mygtukas = Button(langas, text="Daryti", command=daryti)
# status = Label(langas, text="Nieko nedaro...", bd=1, relief=SUNKEN, anchor=W)
# status.pack(side=BOTTOM, fill=X)
#
# mygtukas.pack()
#
# langas.mainloop()

#
# from tkinter import *
# import webbrowser
#
# def callback(url):
#     webbrowser.open_new(url)
#
# root = Tk()
# link1 = Label(root, text="Google Hyperlink", fg="blue", cursor="hand2")
# link1.pack()
# link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))
#
# link2 = Label(root, text="Ecosia Hyperlink", fg="blue", cursor="hand2")
# link2.pack()
# link2.bind("<Button-1>", lambda e: callback("http://www.ecosia.org"))
#
# root.mainloop()

#
#
# from tkinter import *
# from PIL import ImageTk, Image
# import os
#
# root = Tk()
# img = ImageTk.PhotoImage(Image.open("paveiksliukas.JPG"))
# panel = Label(root, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")
# root.mainloop()
#
#
#
#
# import tkinter as tk
#
# class Demo1:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
#         self.button1.pack()
#         self.frame.pack()
#
#     def new_window(self):
#         self.newWindow = tk.Toplevel(self.master)
#         self.app = Demo2(self.newWindow)
#
# class Demo2:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
#         self.quitButton.pack()
#         self.frame.pack()
#
#     def close_windows(self):
#         self.master.destroy()
#
# def main():
#     root = tk.Tk()
#     app = Demo1(root)
#     root.mainloop()
#
# if __name__ == '__main__':
#     main()
#
# import tkinter as tk
#
# class Demo1:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
#         self.button1.pack()
#         self.frame.pack()
#
#     def new_window(self):
#         self.newWindow = tk.Toplevel(self.master)
#         self.app = Demo2(self.newWindow)
#
# class Demo2:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
#         self.quitButton.pack()
#         self.frame.pack()
#
#     def close_windows(self):
#         self.master.destroy()
#
# def main():
#     root = tk.Tk()
#     app = Demo1(root)
#     root.mainloop()
#
# if __name__ == '__main__':
#     main()



# def sumbit():
#     user_input = field1.get()
#     print(user_input)
#     result["text"] = f"Sveikas {user_input}"
#
#
# name = Label(window, text="Enter your name")
# button = Button(window, text="Enter", command=sumbit)
# field1 = Entry(window)
# result = Label(window, text="")
#
# name.pack()
# field1.pack()
# button.pack()
# result.pack()
#
#
# window.mainloop()
from tkinter import *

#
# from tkinter import *
#
#
# def enter_name():
#     write_name.set(field1.get())
#     # print(write_name)
#     output["text"] = f"Labas  {write_name}"
#
# def delete():
#     user_input = field1.get()
#     output["text"] = f""
#
# def restore():
#     output["text"] = f"Labas  {write_name.get()}"
#
# window = Tk()
# write_text = StringVar()
# window.geometry("300x80")
#
#
# menu = Menu(window)
# window.config(menu=menu)
# submenu = Menu(menu, tearoff=0)
#
# menu.add_cascade(label="Menu", menu=submenu)
# submenu.add_command(label="Delete", command=delete)
# submenu.add_command(label="Restore", command=restore)
# submenu.add_separator()
# submenu.add_command(label="Exit")
#
#
# name = Label(window, text="Name")
# field1 = Entry(window)
# button = Button(window, text="Enter", command=enter_name)
# output = Label(window, text="")
# window.bind("<Return>", lambda event: enter_name())
#
#
# # button.pack()
# name.grid(row=0, column=0, sticky=W)
# field1.grid(row=0, column=1, sticky=W)
# button.grid(row=0, column=2, sticky=W)
# output.grid(row=1, column=1, sticky=W)
# window.mainloop()
#






#


from tkinter import Tk, END


def submit():
    user_input.set(field.get())
    result["text"] = f"what is going on? {user_input.get()}"


def delete():
    result["text"] = ""
    field.delete(0, END)


def restore():
    result["text"] = f"what is going on? {user_input.get()}"


window = Tk()
user_input = StringVar()

# def daryti():
#     status["text"] = "Dabar daro"
#
# def status_deleting():
#     status["text"] = "Deleted"
#
#
# menu = Menu(window)
# window.config(menu=menu)
# submenu = Menu(menu, tearoff=0)
# window.geometry("450x200")
#
# menu.add_cascade(label="Menu", menu=submenu)
# submenu.add_command(label="Delete", command=delete)
# submenu.add_command(label="Restore", command=restore)
# submenu.add_separator()
# submenu.add_command(label="Exit", command=window.destroy)
#
# status = Label(window, text="", bd=1, relief=SUNKEN, anchor=W)
# status.pack(side=BOTTOM, fill=X)
#
#
# button = Button(window, text="Enter", command=submit)
# name = Label(window, text="Enter a username")
# field = Entry(window)
# result = Label(window, text="")
#
# window.bind("<Return>", lambda event: submit())
#
#
# field.pack()
# name.pack()
# button.pack()
# result.pack()
#
# window.mainloop()
#
#
# class Tree:
#     def __init__(self, name: str, location: str, height: int):
#         self.name = name
#         self.location = location
#         self.height = height
#
#     def im_green(self):
#         print('I`m very green and big ma boy')
#
#
#
# class BigTree(Tree):
#
#     def introduction(self):
#         print("My name is {self.name}. I live in {self.location} and my height is {self.height} meters.")
#
#
# tree1 = Tree('Oak', 'Lithuania', 17)
# tree2 = BigTree('Spruce', 'Norway', 12)
#
# tree2.introduction()
#
