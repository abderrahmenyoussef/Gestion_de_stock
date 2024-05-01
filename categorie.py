from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox,ttk
import time
from customtkinter import *
import sqlite3

class Categorie:
    def __init__(self, root):
        self.root = root
        self.root.title("Categorie")
        self.root.geometry("1200x600+400+200")
        self.root.config(bg="white")
        self.root.focus_force()

        ###les variables 

        self.var_cat_id=StringVar()
        self.var_nom=StringVar()



        title =Label(self.root,text="Gestion Categorie Produit",font=("goudy old style",40,"bold"),bg="#76CDCD",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10)

         ###base de donnes

        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS categorie (cid INTEGER PRIMARY KEY AUTOINCREMENT,nom text)")
        con.commit()

        ###contenu

        lbl_categorie=Label(self.root,text="Saisir Categorie Produit",font=("times new roman",30),bg="white").place(x=50,y=150)
        txt_categorie= Entry(self.root,textvariable=self.var_nom,font=("times new roman",30),bg="lightyellow").place(x=50,y=230,width=380)

        btn_ajouter=CTkButton(master=self.root,
                                    command=self.ajouter,
                                    text="Ajouter",
                                    font=("times new roman",25,"bold"),
                                    text_color="black",
                                    corner_radius=32,
                                    hover_color="#679436",
                                    fg_color="#8FB43A",
                                    bg_color="white",
                                    height=40,
                                    width=150) 
        btn_ajouter.place(x=350,y=180)
        btn_supprimer= CTkButton(master=self.root, 
                                    command=self.supprimer, 
                                    text="Supprimer",
                                    font=("times new roman",25,"bold"),
                                    text_color="black",
                                    corner_radius=32,
                                    hover_color="#A92831",
                                    fg_color="#CF4146", 
                                    bg_color="white",
                                    height=40,
                                    width=150) 
        btn_supprimer.place(x=515,y=180)

        ###liste categorie

        listeFrame=Frame(self.root,bd=3,relief=RIDGE)
        listeFrame.place(x=900,y=100,height=180,width=600)

        scroll_y=Scrollbar(listeFrame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=Scrollbar(listeFrame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)

        self.categorieliste=ttk.Treeview(listeFrame,columns=("cid",
                                                          "nom",),
                                                          yscrollcommand=scroll_y.set,
                                                          xscrollcommand=scroll_x.set)
        
        scroll_x.config(command=self.categorieliste.xview)
        scroll_y.config(command=self.categorieliste.yview)

        self.categorieliste.heading("cid",text="ID")
        self.categorieliste.heading("nom",text="Nom")

        self.categorieliste["show"]="headings"
        
        self.categorieliste.pack(fill=BOTH,expand=1)

        self.categorieliste.bind("<ButtonRelease-1>",self.get_donnes)

        self.afficher()

        self.cat1=Image.open(r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Images\cat1.jpg")
        self.cat1=self.cat1.resize((700,400),Image.Resampling.LANCZOS)
        self.cat1=ImageTk.PhotoImage(self.cat1)

        self.lbl_ima_cat1=Label(self.root,bd=7,relief=RAISED,image=self.cat1)
        self.lbl_ima_cat1.place(x=50,y=300)

        
        self.cat2=Image.open(r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Images\cat2.jpg")
        self.cat2=self.cat2.resize((700,400),Image.Resampling.LANCZOS)
        self.cat2=ImageTk.PhotoImage(self.cat2)

        self.lbl_ima_cat2=Label(self.root,bd=7,relief=RAISED,image=self.cat2)
        self.lbl_ima_cat2.place(x=770,y=300)

        ###fonction

    def ajouter(self):
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()
        try:
            if self.var_nom.get()=="":
                messagebox.showerror("Erreur","Veillez saisir une categorie de produit")
            else:
                cur.execute("select * from categorie where nom=?",(self.var_nom.get(),)) 
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Erreur","La categorie existe deja")  
                else:
                    cur.execute("insert into categorie (nom) values (?)",(self.var_nom.get(),))
                    con.commit()
                    self.var_cat_id.set("")
                    self.var_nom.set("")
                    self.afficher()
                    messagebox.showinfo("Succés","Enregistrement effectué")

        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}")  

    def afficher(self):
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()
        try:
            cur.execute("select * from categorie")
            rows = cur.fetchall()
            self.categorieliste.delete(*self.categorieliste.get_children())
            for row in rows:
                self.categorieliste.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}")

    def get_donnes(self,ev):    
        r=self.categorieliste.focus()
        contenu=self.categorieliste.item(r)
        row=contenu["values"]  
        self.var_cat_id.set(row[0])
        self.var_nom.set(row[1])

    def supprimer(self):
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()

        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Erreur","Veillez selectionner une categorie a partir de la liste")
            else :
                cur.execute("select * from categorie where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Erreur","L'id n'existe pas")
                else : 
                      op=messagebox.askyesno("Confirmer","Voulez-vous vraiment supprimer?")
                      if op==True:
                        cur.execute("delete from categorie where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        self.afficher()
                        self.var_cat_id.set("")
                        self.var_nom.set("")
                        messagebox.showinfo("Succés","Suppression effectuée")

                





        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}")  




if __name__ == "__main__":
    root = CTk()
    obj = Categorie(root)
    root.mainloop()
