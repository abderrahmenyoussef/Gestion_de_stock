from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import time
from customtkinter import *

class Employe:
    def __init__(self, root):
        self.root = root
        self.root.title("Employe")
        self.root.geometry("1200x600+400+200")
        self.root.config(bg="white")
        self.root.focus_force()


if __name__ == "__main__":
    root = CTk()
    obj = Employe(root)
    root.mainloop()
