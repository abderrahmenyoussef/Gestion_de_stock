from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import time
from customtkinter import *
import sqlite3

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Connexion")
        self.root.geometry("1200x600+200+100")
        self.root.config(bg="white")
        self.root.focus_force()


        login_frame=Frame(self.root,bg="#76CDCD")
        login_frame.place(x=500,y=130,width=500,height=500)

        title =Label(login_frame,text="Connexion",font=("Algerian",40,"bold"),bg="#76CDCD",fg="black").pack(side=TOP,fill=X)

        lbl_id = Label(login_frame,text="ID Employé",font=("times new roman",30,"bold"),bg="#76CDCD").place(x=150,y=100)
        lbl_id = Label(login_frame,text="Mot de passe",font=("times new roman",30,"bold"),bg="#76CDCD").place(x=150,y=200)

        self.txt_id_employ=Entry(login_frame,font=("times new roman",20),bg="lightgray")
        self.txt_id_employ.place(x=125,y=160)
        self.txt_pass_employ=Entry(login_frame,show="*",font=("times new roman",20),bg="lightgray")
        self.txt_pass_employ.place(x=125,y=270)

        connecter_btn = CTkButton(master=self.root,
                                    command=self.connexion,
                                    text="Connexion",
                                    font=("times new roman", 20),
                                    text_color="black",
                                    corner_radius=32,
                                    hover_color="#2F4558",
                                    fg_color="#335F8A",
                                    bg_color="#76CDCD",
                                    height=40,
                                    width=120).place(x=550,y=380)

    def connexion(self):
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()
        try:
            if self.txt_id_employ.get()=="" or self.txt_pass_employ.get()=="":
                messagebox.showerror("Erreur","Veillez donnez votre ID Employé et votre mot de passe")
            else :
                cur.execute("select Type from employe where ID=? AND Password=? AND Type = 'Admin' ",(self.txt_id_employ.get(),self.txt_pass_employ.get()))
                user =cur.fetchone()
                if user==None :
                    messagebox.showerror("Erreur","L'ID Employé ou le mot de passe est incorrecte")
                else :
                        self.root.destroy()
                        os.system("python C:/Users/abdou/Desktop/Gestion_de_stock_et_caisse_enregistreuse/accueil.py")

        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}") 




if __name__ == "__main__":
    root = CTk()
    obj = Login(root)
    root.mainloop()
