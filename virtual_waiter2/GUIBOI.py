#!/usr/bin/env python3

from queue import Queue, Empty
from tkinter import PhotoImage, Tk, Text, END, Button, Frame, Label, Toplevel
from utilities.Initialize_GUI import ProcessOutputReader, MyConsole, ImageLabel
from PIL import ImageTk, Image
from sys import exit
import random

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
    Click Start -> Type 'Manage app execution aliases' 
    -> Switch off the Python App Installer -> Now try executing the program again

'''


# create the root widget
root = Tk()
root.title('NYEW - Waiter for your services')
root.iconphoto(False, PhotoImage(file='./Images/waiter_icon_tkinter_png.png'))
root.config(background='#adefd1')

loading_screen_paths = ['./Images/waiterwaiter.gif', './Images/waiterwaiter2.gif', './Images/waiterwaiter3.gif']
bg = PhotoImage(file='./Images/waiter.png')
# bg_adj = bg.subsample(2, 1)
bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
menu_icon = PhotoImage(file='./Images/menu_icon.png')
waiter_icon = PhotoImage(file='./Images/waiter_icon.png')
exit_icon = PhotoImage(file='./Images/exit_icon.png')

category_icons = ['./Images/starter_icon.png', './Images/burger_icon.png', './Images/pizza_icon.png', './Images/pasta_icon.png', './Images/sandwich_icon.png', './Images/beverage_icon.png', './Images/milkshake_icon.png', './Images/juice_icon.png', './Images/dessert_icon.png', './Images/dip_icon.png']
for c in range(len(category_icons)):
    category_icons[c] = PhotoImage(file=category_icons[c])

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
    
    loading_screen = ImageLabel(console)
    loading_screen.pack()
    loading_screen.load(loading_screen_paths[random.randint(0, 2)])
    # mytext.place(x=0, y=0, relwidth=1, relheight=1)
    loading_screen.after(6000, loading_screen.killMyself)

    console.pack()   # make the console visible
    print('RESTARTING...\n')
    root.mainloop()  # run the TKinter main loop
    
    reader.stop()
    reader.join(timeout=5)  # give thread a chance to exit gracefully

    if reader.is_alive():
        raise RuntimeError("process output reader failed to stop")

def display_menu():
    win = Toplevel()
    win.title('Menu')
    win.iconphoto(False, menu_icon)
    win.config(background='light goldenrod')
    
    starters = Button(win, text="            Starters", cursor='hand2', image=category_icons[0], compound='left', command=starter_menu, bg='pale green', foreground='black', font='Courier')
    burgers = Button(win, text="             Burgers", cursor='hand2', image=category_icons[1], compound='left', command=burger_menu, bg='pale green', foreground='black', font='Courier')
    pizza = Button(win, text="              Pizzas", cursor='hand2', image=category_icons[2], compound='left', command=pizza_menu, bg='pale green', foreground='black', font='Courier')
    pasta = Button(win, text="              Pastas", cursor='hand2', image=category_icons[3], compound='left', command=pasta_menu, bg='pale green', foreground='black', font='Courier')
    sandwich = Button(win, text="Sandwiches and Rolls", cursor='hand2', image=category_icons[4], compound='left', command=sandwich_menu, bg='pale green', foreground='black', font='Courier')
    beverage = Button(win, text="           Beverages", cursor='hand2', image=category_icons[5], compound='left', command=beverage_menu, bg='pale green', foreground='black', font='Courier')
    milkshakes = Button(win, text="          Milkshakes", cursor='hand2', image=category_icons[6], compound='left', command=milkshake_menu, bg='pale green', foreground='black', font='Courier')
    juice = Button(win, text="  Fresh Fruit Juices", cursor='hand2', image=category_icons[7], compound='left', command=juice_menu, bg='pale green', foreground='black', font='Courier')
    dessert = Button(win, text="            Desserts", cursor='hand2', image=category_icons[8], compound='left', command=dessert_menu, bg='pale green', foreground='black', font='Courier')
    dip = Button(win, text="     Dips and Sauces", cursor='hand2', image=category_icons[9], compound='left', command=dip_menu, bg='pale green', foreground='black', font='Courier')

    starters.pack(side="top", fill="x", ipadx='3') 
    burgers.pack(side="top", fill="x", ipadx='3')
    pizza.pack(side="top", fill="x", ipadx='3')
    pasta.pack(side="top", fill="x", ipadx='3')
    sandwich.pack(side="top", fill="x", ipadx='3')
    beverage.pack(side="top", fill="x", ipadx='3')
    milkshakes.pack(side="top", fill="x", ipadx='3')
    juice.pack(side="top", fill="x", ipadx='3')
    dessert.pack(side="top", fill="x", ipadx='3')
    dip.pack(side="top", fill="x", ipadx='3')
    win.mainloop()

def starter_menu():
    starter_obj = Toplevel()
    starter_obj.title("Starter Menu")
    starter_obj.iconphoto(False, category_icons[0])

    image1 = Image.open("./Images/Menu Items/onion_rings.jpg")
    """image2 = Image.open("./Images/Menu Items/chicken_Wings.jpg")
    image3 = Image.open("./Images/Menu Items/chicken_nuggets.jpg")
    image4 = Image.open("./Images/Menu Items/onion_rings.jpg")
    image5 = Image.open("./Images/Menu Items/tomato_soup.jpg")"""
    
    # The (450, 350) is (height, width)
    image1 = image1.resize((450, 350), Image.ANTIALIAS)
    """image2 = image2.resize((450, 350), Image.ANTIALIAS)
    image3 = image3.resize((450, 350), Image.ANTIALIAS)
    image4 = image4.resize((450, 350), Image.ANTIALIAS)
    image5 = image5.resize((450, 350), Image.ANTIALIAS)"""
    my_img1 = ImageTk.PhotoImage(image1)
    """my_img2 = ImageTk.PhotoImage(image2)
    my_img3 = ImageTk.PhotoImage(image3)
    my_img4 = ImageTk.PhotoImage(image4)
    my_img5 = ImageTk.PhotoImage(image5)"""

    #Starter Objects
    starter_obj.my_img1 = my_img1
    """starter_obj.my_img2 = my_img2
    starter_obj.my_img3 = my_img3
    starter_obj.my_img4 = my_img4
    starter_obj.my_img5 = my_img5"""

    #Image list
    #img_list=[my_img1, my_img2, my_img3, my_img4, my_img5]

    my_img1 = Label(starter_obj,image = my_img1)
    my_img1.pack()

    #Action functions
    """def back(number):
        global button_back
        global button_forward
        global my_img1
        my_img1.pack_forget()
        my_img1=Label(starter_obj,image = img_list[number-1]).pack
    def forward(number):
        global button_back
        global button_forward
        global my_img1
        my_img1.pack_forget()
        my_img1=Label(starter_obj,image = img_list[number+1]).pack()

    

    #button_back = Button(starter_obj, text="<<", command = back).pack()
    #button_forward = Button(starter_obj, text=">>", command = lambda: forward(0)).pack()"""

    fries1 = Label(starter_obj, text="French Fries 	     87.62",font=("Courier",18)).pack()
    fries2 = Label(starter_obj, text="Chicken Wings	     109.7",font=("Courier",18)).pack()
    fries3 = Label(starter_obj, text="Chicken Nuggets	    108.86",font=("Courier",18)).pack()
    fries4 = Label(starter_obj, text="Onion Rings	     71.83",font=("Courier",18)).pack()
    fries5 = Label(starter_obj, text="Tomato Soup	    114.05",font=("Courier",18)).pack()
    fries6 = Label(starter_obj, text="Nachos		    103.29",font=("Courier",18)).pack()
    starter_obj.mainloop()

def burger_menu():
    burger_obj = Toplevel()
    burger_obj.title("Burger Menu")
    burger_obj.iconphoto(False, category_icons[1])
    image1 = Image.open("./Images/Menu Items/veg_burger(1080).jpg")
    image1 = image1.resize((450, 350), Image.ANTIALIAS)
    my_img1 = ImageTk.PhotoImage(image1)
    burger_obj.my_img1 = my_img1
    my_img1 = Label(burger_obj,image = my_img1)
    my_img1.pack()
    burger1 = Label(burger_obj, text="Veg Burger	 86.29",font=("Courier",18)).pack()
    burger2 = Label(burger_obj, text="Chicken Burger	115.23",font=("Courier",18)).pack()
    burger3 = Label(burger_obj, text="Hamburger	102.96",font=("Courier",18)).pack()
    burger_obj.mainloop()

def pizza_menu():
    pizza_obj = Toplevel()
    pizza_obj.title("Pizza Menu")
    pizza_obj.iconphoto(False, category_icons[2])
    image1 = Image.open("./Images/Menu Items/tomato_basil_pizza.jpg")
    image1 = image1.resize((450, 350), Image.ANTIALIAS)
    my_img1 = ImageTk.PhotoImage(image1)
    pizza_obj.my_img1 = my_img1
    my_img1 = Label(pizza_obj,image = my_img1)
    my_img1.pack()
    pizza1 = Label(pizza_obj, text="Farmhouse Pizza	      107.82",font=("Courier",18)).pack()
    pizza2 = Label(pizza_obj, text="Mozzarella Pizza       118.5",font=("Courier",18)).pack()
    pizza3 = Label(pizza_obj, text="Tomato basil Pizza    102.02",font=("Courier",18)).pack()
    pizza4 = Label(pizza_obj, text="Pepperoni Pizza	       97.36",font=("Courier",18)).pack()
    pizza_obj.mainloop()

def pasta_menu():
    pasta_obj = Toplevel()
    pasta_obj.title("Pasta Menu")
    pasta_obj.iconphoto(False, category_icons[3])
    image1 = Image.open("./Images/Menu Items/spaghetti.jpg")
    image1 = image1.resize((450, 350), Image.ANTIALIAS)
    my_img1 = ImageTk.PhotoImage(image1)
    pasta_obj.my_img1 = my_img1
    my_img1 = Label(pasta_obj,image = my_img1)
    my_img1.pack()
    pasta1 = Label(pasta_obj, text="Mac-n-Cheese		95.28",font=("Courier",18)).pack()
    pasta1 = Label(pasta_obj, text="Arrabbiata Pasta	 95.4",font=("Courier",18)).pack()
    pasta1 = Label(pasta_obj, text="Spaghetti		71.33",font=("Courier",18)).pack()
    pasta1 = Label(pasta_obj, text="Pesto Pasta		74.13",font=("Courier",18)).pack()
    pasta_obj.mainloop()

def sandwich_menu():
    sandwich_obj = Toplevel()
    sandwich_obj.title("Sandwich and Rolls Menu")
    sandwich_obj.iconphoto(False, category_icons[4])
    image1 = Image.open("./Images/Menu Items/grilled_cheese_sandwich.jpg")
    image1 = image1.resize((450, 350), Image.ANTIALIAS)
    my_img1 = ImageTk.PhotoImage(image1)
    sandwich_obj.my_img1 = my_img1
    my_img1 = Label(sandwich_obj,image = my_img1)
    my_img1.pack()
    sandwich1= Label(sandwich_obj, text="Veg Sandwich		117.28",font=("Courier",18)).pack()
    sandwich2= Label(sandwich_obj, text="Chicken Sandwich   	 92.41",font=("Courier",18)).pack()
    sandwich3= Label(sandwich_obj, text="Grilled Cheese Sandwich	105.55",font=("Courier",18)).pack()
    sandwich4= Label(sandwich_obj, text="Tacos    	         85.76",font=("Courier",18)).pack()
    sandwich5= Label(sandwich_obj, text="Burritos	  	 78.54",font=("Courier",18)).pack()
    sandwich_obj.mainloop()

def beverage_menu():
    beverage_obj = Toplevel()
    beverage_obj.title("Beverage Menu")
    beverage_obj.iconphoto(False, category_icons[5])
    image1 = Image.open("./Images/Menu Items/green_tea.jpg")
    image1 = image1.resize((450, 350), Image.ANTIALIAS)
    my_img1 = ImageTk.PhotoImage(image1)
    beverage_obj.my_img1 = my_img1
    my_img1 = Label(beverage_obj,image = my_img1)
    my_img1.pack()
    beverage1= Label(beverage_obj, text="Coke		55.35",font=("Courier",18)).pack()
    beverage2= Label(beverage_obj, text="Iced Tea	51.77",font=("Courier",18)).pack()
    beverage3= Label(beverage_obj, text="Green Tea	64.42",font=("Courier",18)).pack()
    beverage4= Label(beverage_obj, text="Coffee		64.86",font=("Courier",18)).pack()
    beverage_obj.mainloop()  

def milkshake_menu():
    milkshake_obj = Toplevel()
    milkshake_obj.title("Milkshake Menu")
    milkshake_obj.iconphoto(False, category_icons[6])
    image1 = Image.open("./Images/Menu Items/strawberry_milkshake.jpg")
    image1 = image1.resize((450, 350), Image.ANTIALIAS)
    my_img1 = ImageTk.PhotoImage(image1)
    milkshake_obj.my_img1 = my_img1
    my_img1 = Label(milkshake_obj,image = my_img1)
    my_img1.pack()
    milkshake1= Label(milkshake_obj, text="Oreo Shake	 	54.96",font=("Courier",18)).pack()
    milkshake2= Label(milkshake_obj, text="Strawberry Milkshake	63.62",font=("Courier",18)).pack()
    milkshake3= Label(milkshake_obj, text="Chocolate Milkshake	64.98",font=("Courier",18)).pack()
    milkshake4= Label(milkshake_obj, text="Avocado Milkshake	 54.4",font=("Courier",18)).pack()
    milkshake_obj.mainloop()
    
def juice_menu():
    juice_obj = Toplevel()
    juice_obj.title("Fresh Fruit Juice Menu")
    juice_obj.iconphoto(False, category_icons[7])
    image1 = Image.open("./Images/Menu Items/mango_juice.jpg")
    image1 = image1.resize((450, 350), Image.ANTIALIAS)
    my_img1 = ImageTk.PhotoImage(image1)
    juice_obj.my_img1 = my_img1
    my_img1 = Label(juice_obj,image = my_img1)
    my_img1.pack()
    juice1= Label(juice_obj, text="Apple Juice		39.52",font=("Courier",18)).pack()
    juice2= Label(juice_obj, text="Mango Juice		30.22",font=("Courier",18)).pack()
    juice3= Label(juice_obj, text="Orange Juice		30.59",font=("Courier",18)).pack()
    juice4= Label(juice_obj, text="Lemonade		41.73",font=("Courier",18)).pack()
    juice_obj.mainloop()

def dessert_menu():
    dessert_obj = Toplevel()
    dessert_obj.title("Desserts")
    dessert_obj.iconphoto(False, category_icons[8])
    image1 = Image.open("./Images/Menu Items/blueberry_cheesecake.jpg")
    image1 = image1.resize((450, 350), Image.ANTIALIAS)
    my_img1 = ImageTk.PhotoImage(image1)
    dessert_obj.my_img1 = my_img1
    my_img1 = Label(dessert_obj,image = my_img1)
    my_img1.pack()
    cake1 = Label(dessert_obj, text="Chocolate Cupcake	59.74",font=("Courier",18)).pack()
    cake2 = Label(dessert_obj, text="Sprinkle Donuts		50.47",font=("Courier",18)).pack()
    cake3 = Label(dessert_obj, text="Red velvet Cupcake	64.24",font=("Courier",18)).pack()
    cake4 = Label(dessert_obj, text="Blueberry Cheesecake	46.12",font=("Courier",18)).pack()
    cake4 = Label(dessert_obj, text="Strawberry Ice cream	54.97",font=("Courier",18)).pack()
    dessert_obj.mainloop()

def dip_menu():
    dip_obj = Toplevel()
    dip_obj.title("Dips and Sauces")
    dip_obj.iconphoto(False, category_icons[9])
    image1 = Image.open("./Images/Menu Items/dips.jpg")
    image1 = image1.resize((450, 350), Image.ANTIALIAS)
    my_img1 = ImageTk.PhotoImage(image1)
    dip_obj.my_img1 = my_img1
    my_img1 = Label(dip_obj,image = my_img1)
    my_img1.pack()
    dip1 = Label(dip_obj, text="Guacamole   	   20.84",font=("Courier",18)).pack() 
    dip1 = Label(dip_obj, text="Tomato ketchup	   18.59",font=("Courier",18)).pack() 
    dip1 = Label(dip_obj, text="Mustard		    16.2",font=("Courier",18)).pack() 
    dip1 = Label(dip_obj, text="Barbecue sauce	   18.82",font=("Courier",18)).pack() 
    dip1 = Label(dip_obj, text="Mayonnaise	   12.46",font=("Courier",18)).pack() 
    dip1 = Label(dip_obj, text="Cheesy dip	   12.52",font=("Courier",18)).pack()
    dip_obj.mainloop()

reader.start()   # start the process

loading_screen = ImageLabel(console)
loading_screen.pack()
loading_screen.load(loading_screen_paths[random.randint(0, 2)])
# mytext.place(x=0, y=0, relwidth=1, relheight=1)
loading_screen.after(6000, loading_screen.killMyself)

console.config(background='light yellow')
console.pack()   # make the console visible

class Pad(Frame):
  
    # constructor to add buttons and text to the window
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.toolbar = Frame(self, bg="light goldenrod")
        self.toolbar.pack(side="top", fill="x")

        # this will display the menu to the user
        self.menu_btn = Button(self.toolbar, text="Menu", cursor='hand2', image=menu_icon, compound='left', command=display_menu, bg='lawn green', foreground='black', font='Courier')
        self.menu_btn.pack(side="left", ipadx='6')

        # this will quit the window and exit it
        self.exit_btn = Button(self.toolbar, text="Exit", cursor='hand2', image=exit_icon, compound='left', command=exit, bg='firebrick2', foreground='white', font='Courier')
        self.exit_btn.pack(side='right', ipadx='6')

        # this will restart the waiter in the window
        self.restart_btn = Button(self.toolbar, text="Call Me Again", cursor='hand2', image=waiter_icon, compound='left', command=restart, bg='OliveDrab1', font='Courier')
        self.restart_btn.pack(side="right", ipadx='2')

Pad(root).pack(expand=1, fill='both')   # create toolbars in the frame

root.mainloop()  # run the TkInter main loop

reader.stop()
reader.join(timeout=5)  # give thread a chance to exit gracefully

if reader.is_alive():
    raise RuntimeError("Process output reader failed to stop")
