"""
ZetCode Tkinter tutorial

This script shows a simple window
on the screen.

Author: Rafeh Qazi
Last Modified: April 2016
"""

from tkinter import Tk, Frame, BOTH


class Example(Frame):
    def __int__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
