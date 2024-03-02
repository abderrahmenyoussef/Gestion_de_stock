from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import time

class Accueil :
    def __init__(self,root):
        self.root=root
        self.root.title("Acceuil")
        self.root.geometry("1920x1080")
        self.root.config(bg="white")

        #recuperation de l'image et l'ecrit du titre pour la page d'accueil
        self.icon_title= ImageTk.PhotoImage(file="Images\logo.png")
        titre=Label(self.root,text="Gestion Drugstore",image=self.icon_title,font=("times new roamn",40,"bold"),bg="#29bdc1",anchor="w",padx=20,compound=LEFT).place(x=0,y=0,relwidth=1,height=100)

        #button deconnexion 
        btn_deconnecte=Button(self.root,text="Deconnecter",font=("times new roamn",20,"bold"),cursor="hand2",bg="#d84242").place(x=1330,y=20)

        #heure
        self.lbl_heure=Label(self.root,text="Bienvenu Chez Abdou\t\t Date: DD-MM-YYYY\t\t Heure: HH-MM-SS",font=("times new roamn",15),bg="black",fg="white")
        self.lbl_heure.place(x=0,y=100,relwidth=1,height=40)

        #Menu
        



if __name__=="__main__":
    root=Tk()
    obj=Accueil(root)
    root.mainloop()
