from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import time

class Accueil:
    def __init__(self, root):
        self.root = root
        self.root.title("Acceuil")
        self.root.geometry("1920x1080")
        self.root.config(bg="white")

        # recuperation de l'image et l'ecrit du titre pour la page d'accueil
        self.icon_title = ImageTk.PhotoImage(file="Images\logo.png")
        titre = Label(self.root, text="Gestion Drugstore", image=self.icon_title, font=("times new roman", 30, "bold"),
                      bg="#29bdc1", anchor="w", padx=20, compound=LEFT)
        titre.place(x=0, y=0, relwidth=1, height=50)

        # button deconnexion
        btn_deconnecte = Button(self.root, text="Deconnecter", font=("times new roman", 15, "bold"), cursor="hand2",
                                bg="#d84242")
        btn_deconnecte.place(x=1400, y=5)

        # heure
        self.lbl_heure = Label(self.root,
                               text="Bienvenu Chez Abdou\t\t Date: DD-MM-YYYY\t\t Heure: HH-MM-SS",
                               font=("times new roman", 15), bg="black", fg="white")
        self.lbl_heure.place(x=0, y=50, relwidth=1, height=30)

        # Menu
        self.menulogo = Image.open("Images\menu.jpg")
        self.menulogo = self.menulogo.resize((350, 200), Image.Resampling.LANCZOS)  
        self.menulogo = ImageTk.PhotoImage(self.menulogo)

        Menu_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Menu_Frame.place(x=0, y=80, width=350, height=750)
        lbl_menulog=Label(Menu_Frame,image=self.menulogo)
        lbl_menulog.pack(side=TOP,fill=X)
        self.icon_menu=ImageTk.PhotoImage(file="Images\side.jpg")
        lbl_menu=Label(Menu_Frame,text="Menu",font=("times new roman", 40, "bold"),bg="#eaff7b").pack(side=TOP,fill=X)

        btn_employee=Button(Menu_Frame,text="Empolyé",image=self.icon_menu,padx=10,anchor="w",compound=LEFT,font=("times new roman", 19),bd=5,cursor="hand2",bg="white").pack(side=TOP,fill=X)
        btn_fournisseur=Button(Menu_Frame,text="Fournisseur",image=self.icon_menu,padx=10,anchor="w",compound=LEFT,font=("times new roman", 19),bd=5,cursor="hand2",bg="white").pack(side=TOP,fill=X)
        btn_categorie=Button(Menu_Frame,text="Catégorie",image=self.icon_menu,padx=10,anchor="w",compound=LEFT,font=("times new roman", 19),bd=5,cursor="hand2",bg="white").pack(side=TOP,fill=X)
        btn_produit=Button(Menu_Frame,text="Produit",image=self.icon_menu,padx=10,anchor="w",compound=LEFT,font=("times new roman", 19),bd=5,cursor="hand2",bg="white").pack(side=TOP,fill=X)
        btn_vente=Button(Menu_Frame,text="Vente",image=self.icon_menu,padx=10,anchor="w",compound=LEFT,font=("times new roman", 19),bd=5,cursor="hand2",bg="white").pack(side=TOP,fill=X)
        btn_quitter=Button(Menu_Frame,text="Quitter",image=self.icon_menu,padx=10,anchor="w",compound=LEFT,font=("times new roman", 19),bd=5,cursor="hand2",bg="white").pack(side=TOP,fill=X)
           


if __name__ == "__main__":
    root = Tk()
    obj = Accueil(root)
    root.mainloop()
