
from tkinter import Frame, Button, LEFT, Tk
class QaziButtons:

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

root = Tk()
q = QaziButtons(root)
root.mainloop()
