from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import time
from customtkinter import *

class Accueil:
    def __init__(self, root):
        self.root = root
        self.root.title("Acceuil")
        self.root.geometry("1920x780+0+0")
        self.root.config(bg="white")

        # recuperation de l'image et l'ecrit du titre pour la page d'accueil
        self.icon_title = ImageTk.PhotoImage(file="Images\logo.png")
        titre = Label(self.root, 
                      text="Gestion de Store",
                      image=self.icon_title,
                      font=("times new roman", 30, "bold"),
                      bg="#007FA9", 
                      anchor="w",
                      padx=20, 
                      compound=LEFT)
        titre.place(x=0, y=0, relwidth=1, height=50)

        # button deconnexion
        btn_deconnecte = CTkButton(master=self.root,
                                    text="Deconnecter",
                                    command=self.deconnecter,
                                    text_color="black",
                                    corner_radius=32,
                                    hover_color="#D42633",
                                    fg_color="#d84242",
                                    bg_color="#007FA9",
                                    image=CTkImage(Image.open("Images\dec.png"))) 
        btn_deconnecte.place(x=1390, y=7)

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
        Menu_Frame.place(x=0, y=80, width=350, height=870)
        lbl_menulog=Label(Menu_Frame,image=self.menulogo)
        lbl_menulog.pack(side=TOP,fill=X)
        self.icon_menu=ImageTk.PhotoImage(file="Images\side.jpg")
        lbl_menu=Label(Menu_Frame,text="Menu",font=("times new roman", 40, "bold"),bg="#eaff7b").pack(side=TOP,fill=X)

        btn_employee=Button(Menu_Frame,
                            text="Empolyé",
                            command=self.employe,
                            image=self.icon_menu,
                            padx=10,
                            anchor="w",
                            compound=LEFT,
                            font=("times new roman", 19),
                            bd=5,cursor="hand2",
                            bg="white",
                            height=84).pack(side=TOP,fill=X)
        btn_fournisseur=Button(Menu_Frame,
                               text="Fournisseur",
                               command=self.fournisseur,
                               image=self.icon_menu,
                               padx=10,
                               anchor="w",
                               compound=LEFT,
                               font=("times new roman", 19),
                               bd=5,
                               cursor="hand2",
                               bg="white",
                               height=84).pack(side=TOP,fill=X)
        btn_categorie=Button(Menu_Frame,
                             text="Catégorie",
                             command=self.categorie,
                             image=self.icon_menu,
                             padx=10,
                             anchor="w",
                             compound=LEFT,
                             font=("times new roman", 19),
                             bd=5,cursor="hand2",
                             bg="white",
                             height=84).pack(side=TOP,fill=X)
        btn_produit=Button(Menu_Frame,
                           text="Produit",
                           command=self.produit,
                           image=self.icon_menu,padx=10,
                           anchor="w",
                           compound=LEFT,
                           font=("times new roman", 19),
                           bd=5,
                           cursor="hand2",
                           bg="white",
                           height=84).pack(side=TOP,fill=X)
        btn_vente=Button(Menu_Frame,
                         text="Vente",
                         command=self.vente,
                         image=self.icon_menu,
                         padx=10,
                         anchor="w",
                         compound=LEFT,
                         font=("times new roman", 19),
                         bd=5,
                         cursor="hand2",
                         bg="white",
                         height=84).pack(side=TOP,fill=X)
        btn_quitter=Button(Menu_Frame,
                           text="Quitter",
                           command=self.quitter,
                           image=self.icon_menu,
                           padx=10,
                           anchor="w",
                           compound=LEFT,
                           font=("times new roman", 19),
                           bd=5,
                           cursor="hand2",
                           bg="white",
                           height=67).pack(side=TOP,fill=X)

        #contenu 

        self.lbl_totalemploye=Label(self.root,
                                    text="Total Employé \n[0]",
                                      bg="#344D59" , 
                                      bd=5, 
                                      relief=RAISED,
                                      fg="white",
                                      font=("goudy old style",20,"bold"))   
        self.lbl_totalemploye.place(x=400,y=200,height=150,width=300)
        
        self.lbl_totalfournisseur=Label(self.root,
                                        text="Total Fournisseur \n[0]",
                                         bg="#7A90A4" , 
                                         bd=5, relief=RAISED,
                                         fg="white",
                                         font=("goudy old style",20,"bold"))   
        self.lbl_totalfournisseur.place(x=750,y=200,height=150,width=300)

        self.lbl_totalcategorie=Label(self.root,
                                      text="Total Catégorie \n[0]", 
                                      bg="#606C5A" , 
                                      bd=5, 
                                      relief=RAISED,
                                      fg="white",
                                      font=("goudy old style",20,"bold"))   
        self.lbl_totalcategorie.place(x=1100,y=200,height=150,width=300)

        self.lbl_totalproduit=Label(self.root,
                                    text="Total Produit \n[0]", 
                                    bg="#709CA7" , 
                                    bd=5, 
                                    relief=RAISED,
                                    fg="white",
                                    font=("goudy old style",20,"bold"))   
        self.lbl_totalproduit.place(x=1450,y=200,height=150,width=300)

        self.lbl_totalvente=Label(self.root,
                                  text="Total Vente \n[0]", 
                                  bg="#137C8B" , 
                                  bd=5, 
                                  relief=RAISED,
                                  fg="white",
                                  font=("goudy old style",20,"bold"))   
        self.lbl_totalvente.place(x=900,y=400,height=150,width=300)
        
        #footer

        lbl_footer=Label(self.root, 
                         text="Developper par Youssef Abderrahmen \t\t\tabderrahmen.youssef@polytechnicien.tn\t\t\t +21699578783\n\t\tCopyright 2024",
                         font=("times new roman",15),
                         bg="black",
                         fg="white").pack(side=BOTTOM,fill=X)

    #fonction pour appeler les autres pages

    def employe(self):
        self.obj=os.system("python C:/Users/abdou/Desktop/Gestion_de_stock_et_caisse_enregistreuse/employe.py")

    def categorie(self):
        self.obj=os.system("python C:/Users/abdou/Desktop/Gestion_de_stock_et_caisse_enregistreuse/categorie.py")

    def fournisseur(self):
        self.obj=os.system("python C:/Users/abdou/Desktop/Gestion_de_stock_et_caisse_enregistreuse/fournisseur.py")

    def produit(self):
        self.obj=os.system("python C:/Users/abdou/Desktop/Gestion_de_stock_et_caisse_enregistreuse/produit.py")

    def vente(self):
        self.obj=os.system("python C:/Users/abdou/Desktop/Gestion_de_stock_et_caisse_enregistreuse/vente.py")  

    def quitter(self):
        self.root.destroy() 

    def deconnecter(self):
        self.root.destroy()    
        self.obj=os.system("python C:/Users/abdou/Desktop/Gestion_de_stock_et_caisse_enregistreuse/login.py")         


if __name__ == "__main__":
    root = CTk()
    obj = Accueil(root)
    root.mainloop()
