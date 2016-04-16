from tkinter import Tk, Label, Button
counter = 0

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text = "Like a boss")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.inc_button = Button(master, text="Count", command=self.inc)
        self.inc_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def inc(self):
        global counter
        counter += 1
        print(counter)


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
