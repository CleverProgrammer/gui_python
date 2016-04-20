"""
Full tkinter tutorial.

This tutorial shows how to build
things using tkinter. Each function
demonstrates unique ideas.

Author: Rafeh Qazi
Last Modified: April 2016
"""

from tkinter import *

def fitting_widgets():
    root = Tk()
    one = Label(root, text="First Window Ever",
                fg="green", bg="black")
    one.pack()
    two = Label(root, text="Second button",
                fg="white", bg="blue")
    two.pack(fill=X)
    root.mainloop()


def grid_layout():
    root = Tk()

    # Create labels and input fields
    label_1 = Label(root, text="Name")
    label_2 = Label(root, text="Password")
    entry_1 = Entry(root)
    entry_2 = Entry(root)

    # Put labels in a grid. N,E,S,W (North, East, South...)
    label_1.grid(row=0, sticky=E)
    label_2.grid(row=1, sticky=E)

    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)

    root.mainloop()


def func_2_button():
    """Binding functions to layouts."""
    def printHello():
        print("Hello Everyone!!")

    root = Tk()
    button_1 = Button(root, text="Print Hello",
                      command=printHello)
    button_1.pack()
    root.mainloop()


def event_2_button():
    """
    Alternative binding functions to layout.
    This responds to an event. Also notice that
    command=printHello is not there now.
    """
    def printHello(event):
        print("Hello Everyone!!")

    root = Tk()
    button_1 = Button(root, text="Print Hello")
    button_1.bind("<Button-1>", printHello)
    button_1.bind("<Button-2>", printHello)
    button_1.pack()
    root.mainloop()

def mouse_click_events():
    """
    Bind multiple values to buttons
    """
    def left_click(event):
        print("Left click!")

    def right_click(event):
        print("Right click!")

    root = Tk()

    frame = Frame(root, width=300, height=250)
    frame.bind("<Button-1>", left_click)
    frame.bind("<Button-2>", right_click)
    frame.pack()

    root.mainloop()

class QaziButtons:
    """
    Object Oriented Programming approach to tkinter.
    """

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,
                                  text="print name",
                                  command=self.print_msg)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame,
                                 text="quit",
                                 command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def print_msg(self):
        print("Hi, this is a message!")

def classy_QaziButtons():
    """
    Run the class instance of QaziButtons.
    """
    root = Tk()
    q = QaziButtons(root)
    root.mainloop()

def drop_down_menu():
    """
    Little drop-down menu example.
    """

    def do_nothing():
        print("Ok ok I won't...")

    root = Tk()

    menu = Menu(root)
    root.config(menu=menu)

    sub_menu = Menu(menu)
    menu.add_cascade(label="File", menu=sub_menu)

    sub_menu.add_cascade(label="New Project...",
                         command=do_nothing)

    sub_menu.add_cascade(label="New...",
                         command=do_nothing)
    sub_menu.add_separator()
    sub_menu.add_command(label="Exit",
                         command=do_nothing)

    edit_menu = Menu(menu)
    menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Redo")

    # ** TOOLBAR **
    toolbar = Frame(root, bg="grey")
    insert_button = Button(toolbar, text="Insert Image", command=do_nothing)
    insert_button.pack(side=LEFT, padx=5, pady=5)

    print_button = Button(toolbar, text="Print", command=do_nothing)
    print_button.pack(side=LEFT, padx=5, pady=5)

    toolbar.pack(side=TOP, fill=X)

    # ** STATUS BAR **
    status = Label(root, text="You have written 100 words... NOT!", bd=1,
                   relief=SUNKEN, anchor=W)
    status.pack(side=BOTTOM, fill=X)


    root.geometry("250x100")
    root.mainloop()


def shapes_graphics():
    """
    Basic shapes and graphics.
    """

    root = Tk()
    def delete_black_box(event):
        canvas.delete(black_box)

    def delete_all(event):
        canvas.delete(ALL)

    button_1 = Button(root, text="Delete Black Box", padx=15, pady=15)
    button_1.bind("<Button-1>", delete_black_box)
    button_1.pack(side=TOP)

    button_2 = Button(root, text="Delete ALL", padx=33, pady=15)
    button_2.bind("<Button-1>", delete_all)
    button_2.pack(side=TOP)

    canvas = Canvas(root, width=300, height=150)
    canvas.pack()
    size = 30
    black_box = canvas.create_rectangle(30, 30, 30 + size, 30 + size, fill="black")
    green_box = canvas.create_rectangle(70, 70, 70+size, 70+size, fill="green")

    root.mainloop()

if __name__ == '__main__':
    # fitting_widgets()
    # grid_layout()
    # func_2_button()
    # event_2_button()
    # mouse_click_events()
    # classy_QaziButtons()
    # drop_down_menu()
    shapes_graphics()
