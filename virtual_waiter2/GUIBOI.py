#!/usr/bin/env python3

from queue import Queue, Empty
from tkinter import PhotoImage, Tk, Text, END, Button, Frame, Label
from utilities.Initialize_GUI import ProcessOutputReader, MyConsole
from PIL import ImageTk, Image
from sys import exit
import ctypes

'''
    Nyew: Not Your Everyday Waiter
    
    A virtual waiter aims to take on the responsibilities and functionality of a waiter in
    a restaurant, through the use of machine learning models.
    
    Developed By: Batch-23
    
    PRANAV G V
    SKANDA N KASHYAP
    SUBHAYAN MUKHOPADHYAY
    SWATHI K S

If you're using a Windows PC and you get an error when you run this program
asking you to remove app execution aliases, do the following:
Click Start -> type 'Manage app execution aliases' 
-> switch off the Python App Installer -> now try executing the program again

'''


# create the root widget
root = Tk()
root.title('NYEW - Waiter for your services')
root.iconphoto(False, PhotoImage(file='./Images/waiter_icon_tkinter_png.png'))
root.config(background='#adefd1')
# label1 = Label(root, image=ImageTk.PhotoImage(file='./Images/waiter.png'))
# label1.place(root)

# create a queue for sending the lines from the process output reader thread
# to the TkInter main thread
line_queue = Queue(maxsize=1000)

# create a process output reader
try:
    reader = ProcessOutputReader(line_queue, 'python', params=[' -u ', 'waiter.py'])
except TypeError:
    reader = ProcessOutputReader(line_queue, 'python -u waiter.py')

# create a console
console = MyConsole(root, line_queue)

def restart():
    # re-initialize reader as a new process
    try:
        reader = ProcessOutputReader(line_queue, 'python', params=[' -u ', 'waiter.py'])
    except TypeError:
        reader = ProcessOutputReader(line_queue, 'python -u waiter.py')
    # if not reader.is_alive():
    reader.start()   # start the process
    console.pack()   # make the console visible
    print('RESTARTING...\n')
    root.mainloop()  # run the TKinter main loop
    
    reader.stop()
    reader.join(timeout=5)  # give thread a chance to exit gracefully

    if reader.is_alive():
        raise RuntimeError("process output reader failed to stop")

def display_menu():
    win = Tk()
    win.title('Menu')
    
    starters = Button(win, text="Starters", command=starter_menu)
    burgers = Button(win, text="Burgers", command=burger_menu)
    pizza = Button(win, text="Pizzas", command=pizza_menu)
    pasta = Button(win, text="Pastas", command=pasta_menu)
    sandwich = Button(win, text="Sandwiches and Rolls", command=sandwich_menu)
    beverage = Button(win, text="Beverages", command=beverage_menu)
    milkshakes = Button(win, text="Milkshakes", command=milkshake_menu)
    juice = Button(win, text="Fresh Fruit Juices", command=juice_menu)
    dessert = Button(win, text="Dessets", command=dessert_menu)
    dip = Button(win, text="Dips and Sauses", command=dip_menu)

    starters.pack() 
    burgers.pack()
    pizza.pack()
    pasta.pack()
    sandwich.pack()
    beverage.pack()
    milkshakes.pack()
    juice.pack()
    dessert.pack()
    dip.pack()
    win.mainloop()

def starter_menu():
    starter_obj = Tk()
    starter_obj.title("Starter Menu")
    fries1 = Label(starter_obj, text="French Fries 	87.62").pack()
    fries2 = Label(starter_obj, text="Chicken Wings	109.7").pack()
    fries3 = Label(starter_obj, text="Chicken Nuggets	108.86").pack()
    fries4 = Label(starter_obj, text="Onion Rings	71.83").pack()
    fries5 = Label(starter_obj, text="Tomato Soup	114.05").pack()
    fries6 = Label(starter_obj, text="Nachos		103.29").pack()
    starter_obj.mainloop()

def burger_menu():
    burger_obj = Tk()
    burger_obj.title("Burger Menu")
    burger1 = Label(burger_obj, text="Veg Burger	86.29").pack()
    burger2 = Label(burger_obj, text="Chicken Burger	115.23").pack()
    burger3 = Label(burger_obj, text="Hamburger		102.96").pack()
    burger_obj.mainloop()

def pizza_menu():
    pizza_obj = Tk()
    pizza_obj.title("Pizza Menu")
    pizza1 = Label(pizza_obj, text="Farmhouse Pizza	    107.82").pack()
    pizza2 = Label(pizza_obj, text="Mozzarella Pizza		118.5").pack()
    pizza3 = Label(pizza_obj, text="Tomato basil Pizza		102.02").pack()
    pizza4 = Label(pizza_obj, text="Pepperoni Pizza		97.36").pack()
    pizza_obj.mainloop()

def pasta_menu():
    pasta_obj = Tk()
    pasta_obj.title("Pasta Menu")
    pasta1 = Label(pasta_obj, text="Mac-n-Cheese		95.28").pack()
    pasta1 = Label(pasta_obj, text="Arrabbiata Pasta		95.4").pack()
    pasta1 = Label(pasta_obj, text="Spaghetti		71.33").pack()
    pasta1 = Label(pasta_obj, text="Pesto Pasta		74.13").pack()
    pasta_obj.mainloop()

def sandwich_menu():
    sandwich_obj = Tk()
    sandwich_obj.title("Sandwich and Rolls Menu")
    sandwich1= Label(sandwich_obj, text="Veg Sandwich		117.28").pack()
    sandwich2= Label(sandwich_obj, text="Chicken Sandwich		92.41").pack()
    sandwich3= Label(sandwich_obj, text="Grilled Cheese Sandwich	105.55").pack()
    sandwich4= Label(sandwich_obj, text="Tacos		85.76").pack()
    sandwich5= Label(sandwich_obj, text="Burritos		78.54").pack()
    sandwich_obj.mainloop()

def beverage_menu():
    beverage_obj = Tk()
    beverage_obj.title("Beverage Menu")
    beverage1= Label(beverage_obj, text="Coke	Beverages menu	55.35").pack()
    beverage2= Label(beverage_obj, text="Iced Tea	Beverages menu	51.77").pack()
    beverage3= Label(beverage_obj, text="Green Tea	Beverages menu	64.42").pack()
    beverage4= Label(beverage_obj, text="Coffee	Beverages menu	64.86").pack()
    

def milkshake_menu():
    milkshake_obj = Tk()
    milkshake_obj.title("Milkshake Menu")
    milkshake1= Label(milkshake_obj, text="Coke	Beverages menu	55.35").pack()
    milkshake2= Label(milkshake_obj, text="Coke	Beverages menu	55.35").pack()
    milkshake3= Label(milkshake_obj, text="Coke	Beverages menu	55.35").pack()
    milkshake4= Label(milkshake_obj, text="Coke	Beverages menu	55.35").pack()
    
def juice_menu():
    fries = Label(root, text="French Fries 	87.62")
    fries.pack()
def dessert_menu():
    fries = Label(root, text="French Fries 	87.62")
    fries.pack()
def dip_menu():
    fries = Label(root, text="French Fries 	87.62")
    fries.pack()

reader.start()   # start the process
console.pack()   # make the console visible

class Pad(Frame):
  
    # constructor to add buttons and text to the window
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.toolbar = Frame(self, bg="light goldenrod")
        self.toolbar.pack(side="top", fill="x")

        # this will display the menu to the user
        self.menu_btn = Button(self.toolbar, text="Menu", cursor='hand2', command=display_menu, bg='lawn green', foreground='black', font='Courier')
        self.menu_btn.pack(side="left", ipadx='4')

        # this will quit the window and exit it
        self.exit_btn = Button(self.toolbar, text="Exit", cursor='hand2', command=exit, bg='firebrick2', foreground='white', font='Courier')
        self.exit_btn.pack(side='right', ipadx='4')

        # this will restart the waiter in the window
        self.restart_btn = Button(self.toolbar, text="Call Me Again", cursor='hand2', command=restart, bg='OliveDrab1', font='Courier')
        self.restart_btn.pack(side="right")

Pad(root).pack(expand=1, fill='both')   # create toolbars in the frame

root.mainloop()  # run the TkInter main loop

reader.stop()
reader.join(timeout=5)  # give thread a chance to exit gracefully

if reader.is_alive():
    raise RuntimeError("Process output reader failed to stop")
