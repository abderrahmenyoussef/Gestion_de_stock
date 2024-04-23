from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox,ttk
import time
from customtkinter import *
import sqlite3

class Fournisseur:
    def __init__(self, root):
        self.root = root
        self.root.title("Fournisseur")
        self.root.geometry("1200x600+400+200")
        self.root.config(bg="white")
        self.root.focus_force()

        ###base de donnees

        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS fournisseur (forid text PRIMARY KEY,nom text,conatct text,description text)")
        con.commit()

        ###les variables
        self.var_fourni_id=StringVar()
        self.var_recherche_text=StringVar()
        self.var_nom=StringVar()
        self.var_contact=StringVar()

        ###option recherche
        reche_option = Label(self.root, text="Recherche par ID Fournisseur",font=("times new roman",20),bg="white")
        reche_option.place(x=700,y=80)

        recher_text=Entry(self.root,textvariable=self.var_recherche_text,font=("times new roman",15),bg="lightyellow").place(x=1050,y=80,height=40)
        rech_btn=CTkButton(self.root,
                           command=self.rechrche,
                           width=100,
                           height=35,
                            text="Rechercher",
                            text_color="white",
                            fg_color="#226D68",
                            hover_color="#18534F",
                            bg_color="white").place(x=1010,y=65)
        tous= CTkButton(self.root, 
                        command=self.afficher,
                        text="Tous",
                        width=25,
                        height=35,                        
                        text_color="black",
                        fg_color="#FEEAA1",
                        hover_color="#D6955B",
                        bg_color="white").place(x=1115,y=65)
        

        ### titre 
        titre=Label(self.root,
                    text="Formulaire Fournisseur",
                    font=("times new roman",20),
                    cursor="hand2",
                    bg="#76CDCD").place(x=0,y=0,width=1499)
        

        ### contenu 

        #ligne1
        lbl_fourid = Label(self.root,text="ID Fournisseur",font=("goudy old style",20),bg="white").place(x=50,y=70)
        self.txt_fourid=Entry(self.root,textvariable=self.var_fourni_id,font=("goudy old style",20),bg="lightyellow")
        self.txt_fourid.place(x=250,y=70,width=250)

         #ligne2
        lbl_nom = Label(self.root,text="Nom",font=("goudy old style",20),bg="white").place(x=50,y=140)
        txt_nom=Entry(self.root,textvariable=self.var_nom,font=("goudy old style",20),bg="lightyellow").place(x=250,y=140,width=250)


         #ligne3
        lbl_contact = Label(self.root,text="Contact",font=("goudy old style",20),bg="white").place(x=50,y=210)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",20),bg="lightyellow").place(x=250,y=210,width=250)

         #ligne4
        lbl_description = Label(self.root,text="Description",font=("goudy old style",20),bg="white").place(x=50,y=280)
        self.txt_description=Text(self.root,font=("goudy old style",20),bg="lightyellow")
        self.txt_description.place(x=250,y=280,width=600,height=180)

        ##button
        self.ajout_btn = CTkButton(self.root,
                                   command=self.ajouter,
                                    state="normal",
                                    text="Ajouter",
                                    font=("times new roman",20,"bold"),
                                    text_color="black",
                                    corner_radius=32,
                                    hover_color="#679436",
                                    fg_color="#8FB43A",
                                    bg_color="white",
                                    height=40) 
        self.ajout_btn.place(x=10,y=380)
        self.modifier_btn = CTkButton(self.root,
                                    command=self.modifier,  
                                    state="disabled",
                                    text="Modifier",
                                    font=("times new roman",20,"bold"),
                                    text_color="black",
                                    corner_radius=32,
                                    hover_color="#EBBD04",
                                    fg_color="#FEE552",
                                    bg_color="white",
                                    height=40) 
        self.modifier_btn.place(x=190,y=380)
        self.supprimer_btn = CTkButton(self.root,
                                    command=self.supprimer,
                                    state="disabled",   
                                    text="Supprimer",
                                    font=("times new roman",20,"bold"),
                                    text_color="black",
                                    corner_radius=32,
                                    hover_color="#A92831",
                                    fg_color="#CF4146", 
                                    bg_color="white",
                                    height=40) 
        self.supprimer_btn.place(x=370,y=380)
        reni_btn = CTkButton(self.root,
                                    command=self.rein,
                                    text="Reinitialiser",
                                    font=("times new roman",20,"bold"),
                                    text_color="black",
                                    corner_radius=32,
                                    hover_color="#D5CD90",
                                    fg_color="#EEEACB",
                                    bg_color="white",
                                    height=40) 
        reni_btn.place(x=550,y=380)

        #### liste fournisseur

        listeFrame=Frame(self.root,bd=3,relief=RIDGE)
        listeFrame.place(x=900,y=150,height=500,width=600)

        scroll_y=Scrollbar(listeFrame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=Scrollbar(listeFrame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)

        self.fournisseurlsite=ttk.Treeview(listeFrame,columns=("forid","nom","contact","description"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
    
        scroll_x.config(command=self.fournisseurlsite.xview)
        scroll_y.config(command=self.fournisseurlsite.yview)

        self.fournisseurlsite.heading("forid",text="ID")
        self.fournisseurlsite.heading("nom",text="nom")
        self.fournisseurlsite.heading("contact",text="contact")
        self.fournisseurlsite.heading("description",text="decription")

        self.fournisseurlsite["show"]="headings"

        self.fournisseurlsite.pack(fill=BOTH,expand=1)

        self.fournisseurlsite.bind("<ButtonRelease-1>",self.get_donnes)

        self.afficher()

    ###fonction

    def ajouter(self):
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()
        try:
            if self.var_fourni_id.get()=="" or self.var_nom.get()=="" or self.var_contact.get()=="":
                messagebox.showerror("Erreur", "Veillez mettre un ID, nom et conatct")
            else :
                cur.execute("select * from fournisseur where forid=?",(self.var_fourni_id.get(),))    
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Erreur", "L'ID du Fournisseur existe déja")
                else:
                    cur.execute("insert into fournisseur(forid ,nom ,conatct ,description) values(?,?,?,?)",
                                (self.var_fourni_id.get(),
                                 self.var_nom.get(),
                                 self.var_contact.get(),
                                 self.txt_description.get("1.0",END)))
                    con.commit()
                    self.afficher()
                    messagebox.showinfo("Succés","Ajout effectué avec succés")

        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}")   

    def afficher(self):
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()
        try:
            cur.execute("select * from fournisseur")
            rows = cur.fetchall()
            self.fournisseurlsite.delete(*self.fournisseurlsite.get_children())
            for row in rows:
                self.fournisseurlsite.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}")

    def get_donnes(self,ev):
        self.ajout_btn.configure(state="disabled")
        self.supprimer_btn.configure(state="normal")
        self.modifier_btn.configure(state="normal")

        self.txt_fourid.config(state="readonly")    
        r=self.fournisseurlsite.focus()
        contenu=self.fournisseurlsite.item(r)
        row=contenu["values"]  

        self.var_fourni_id.set(row[0]),
        self.var_nom.set(row[1]),
        self.var_contact.set(row[2]),
        self.txt_description.delete("1.0",END),
        self.txt_description.insert(END,row[3]),

    def modifier(self):   
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()
        try:
            cur.execute("update fournisseur set nom=? ,conatct=? ,description=? where forid=? ",
                        (
                                 self.var_nom.get(),
                                 self.var_contact.get(),
                                 self.txt_description.get("1.0",END),
                                 self.var_fourni_id.get(),))
            con.commit()
            self.afficher()
            messagebox.showinfo("Succés","Modification effectué avec succés")

        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}") 

    def supprimer(self):
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()

        try:
            op=messagebox.askyesno("Confirmer","Voulez-vous vraiment supprimer?")
            if op==True:
                cur.execute("delete from fournisseur where forid=?",(self.var_fourni_id.get(),))
                con.commit()
                self.afficher()
                messagebox.showinfo("Succés","Suppression effectuée")

        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}")  

    def rein(self):
                                 self.var_fourni_id.set("")
                                 self.var_nom.set("")
                                 self.var_contact.set("")
                                 self.var_contact.set("")
                                 self.var_recherche_text.set("")
                                 self.txt_description.delete("1.0",END)
                                 self.txt_fourid.config(state="normal")
                                 self.ajout_btn.configure(state="normal")   
                                 self.modifier_btn.configure(state="disabled") 
                                 self.supprimer_btn.configure(state="disabled")

    def rechrche(self):
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()

        try:
             
             if self.var_recherche_text.get()=="":
                  messagebox.showerror("Erreur","Veillez saisir dans le champ de recherche")
             else :
                  cur.execute("select * from fournisseur where forid=?",(self.var_recherche_text.get(),))  
                  row=cur.fetchone()
                  if row!=None:
                       self.fournisseurlsite.delete(*self.fournisseurlsite.get_children())   
                       self.fournisseurlsite.insert("",END,values=row)
                  else :
                       messagebox.showerror("Erreur","Aucun resultat trouvé")          
             

         
        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}")  




















if __name__ == "__main__":
    root = CTk()
    obj = Fournisseur(root)
    root.mainloop()
