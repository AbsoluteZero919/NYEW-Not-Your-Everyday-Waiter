#!/usr/bin/env python3

from queue import Queue, Empty
from tkinter import PhotoImage, Tk, Text, END, Button, Frame
from utilities.Initialize_GUI import ProcessOutputReader, MyConsole

# create the root widget
root = Tk()
root.title('NYEW - Waiter for your services')
root.iconphoto(False, PhotoImage(file='./Images/waiter icon tkinter png.png'))
root.config(background='#adefd1')
# create a queue for sending the lines from the process output reader thread
# to the TkInter main thread
line_queue = Queue(maxsize=1000)

# create a process output reader
reader = ProcessOutputReader(line_queue, 'python', params=[' -u ', 'waiter.py'])

# create a console
console = MyConsole(root, line_queue)

def restart():
    # re-initialize reader as a new process
    reader = ProcessOutputReader(line_queue, 'python', params=[' -u ', 'waiter.py'])
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
    # Write your menu function in here
    # If you want to include any images, they're in this same folder as well
    # 
    # 
    # 
    pass

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
