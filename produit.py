from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox,ttk
import time
from customtkinter import *
import sqlite3

class Produit:
    def __init__(self, root):
        self.root = root
        self.root.title("Produit")
        self.root.geometry("1200x600+400+200")
        self.root.config(bg="white")
        self.root.focus_force()

        ###base de donnees

        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS produit (pid INTEGER PRIMARY KEY AUTOINCREMENT,categorie text,fournisseur text,nom text,prix text,quantite text,statut text)")
        con.commit()

        ### les variables 

        self.var_recherche_type=StringVar()
        self.var_recherche_txt=StringVar()
        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_four=StringVar()
        self.var_nom=StringVar()
        self.var_prix=StringVar()
        self.var_qte=StringVar()
        self.var_satut=StringVar()

        self.four_liste=[]
        self.liste_fou()







        produit_frame= Frame(self.root, bd=2,relief=RIDGE,bg="white")
        produit_frame.place(x=10,y=10,width=670,height=725)

        titre=Label(produit_frame,text="Détails Produit",font=("goudy old style",25,"bold"),bg="#76CDCD").pack(side=TOP,fill=X)

        lbl_categorie=Label(produit_frame,text="Catégorie",font=("goudy old style",25),bg="white").place(x=30,y=80)
        lbl_fournisseur=Label(produit_frame,text="Fournisseur",font=("goudy old style",25),bg="white").place(x=30,y=150)
        lbl_nomproduit=Label(produit_frame,text="Nom",font=("goudy old style",25),bg="white").place(x=30,y=220)
        lbl_prix=Label(produit_frame,text="Prix",font=("goudy old style",25),bg="white").place(x=30,y=290)
        lbl_qte=Label(produit_frame,text="Quantité",font=("goudy old style",25),bg="white").place(x=30,y=360)
        lbl_statut=Label(produit_frame,text="Statut",font=("goudy old style",25),bg="white").place(x=30,y=430)

        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()
        cur.execute("select nom from categorie")
        rows=cur.fetchall()


        txt_categorie=ttk.Combobox(produit_frame,textvariable=self.var_cat,values=rows,state="r",justify=CENTER,font=("goudy old style",20))
        txt_categorie.place(x=210,y=80,width=250)
        txt_categorie.set("Select")



        txt_fourniseeur=ttk.Combobox(produit_frame,textvariable=self.var_four,values=self.four_liste,state="r",justify=CENTER,font=("goudy old style",20))
        txt_fourniseeur.place(x=210,y=150,width=250)
        txt_fourniseeur.current(0)

        txt_nom=Entry(produit_frame,textvariable=self.var_nom,font=("goudy old style",20),bg="lightyellow").place(x=210,y=230,width=250)
    
        txt_prix=Entry(produit_frame,textvariable=self.var_prix,font=("goudy old style",20),bg="lightyellow").place(x=210,y=300,width=250)

        txt_qte=Entry(produit_frame,textvariable=self.var_qte,font=("goudy old style",20),bg="lightyellow").place(x=210,y=370,width=250)

        txt_statut=ttk.Combobox(produit_frame,values=["Active","Inactive"],textvariable=self.var_satut,state="r",justify=CENTER,font=("goudy old style",20))
        txt_statut.place(x=210,y=430,width=250)
        txt_statut.current(0)

        ###les buttons

        self.btn_ajouter=CTkButton(master=produit_frame,
                                    command=self.ajouter,
                                    state="normal",
                                    text="Ajouter",
                                    font=("times new roman",20,"bold"),
                                    text_color="black",
                                    corner_radius=32,
                                    hover_color="#679436",
                                    fg_color="#8FB43A",
                                    bg_color="white",
                                    height=40,
                                    width=110) 
        self.btn_ajouter.place(x=10,y=400)
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
                                    height=40,
                                    width=100) 
        self.modifier_btn.place(x=130,y=410)
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
                                    height=40,
                                    width=100) 
        self.supprimer_btn.place(x=250,y=410)
        reni_btn = CTkButton(self.root,
                                    command=self.rein,
                                    text="Reinitialiser",
                                    font=("times new roman",20,"bold"),
                                    text_color="black",
                                    corner_radius=32,
                                    hover_color="#D5CD90",
                                    fg_color="#EEEACB",
                                    bg_color="white",
                                    height=40,
                                    width=100) 
        reni_btn.place(x=390,y=410)

        ### frame recherche

        rech_frame=LabelFrame(self.root,text="Recherche Produit",font=("times new roman",20),bd=2,relief=RIDGE,bg="white")
        rech_frame.place(x=700,y=10,width=750,height=90)

        txt_rech_option=ttk.Combobox(rech_frame,values=["categorie","fournisseur","nom"],textvariable=self.var_recherche_type,state="r",justify=CENTER,font=("goudy old style",20))
        txt_rech_option.place(x=10,y=10,width=200)
        txt_rech_option.current(0)

        txt_rech=Entry(rech_frame,textvariable=self.var_recherche_txt,font=("goudy old style",20),bg="lightyellow").place(x=235,y=10,width=250)

        recherche= CTkButton(master=rech_frame,
                              command=self.recherche,
                              text="Rechercher",
                              text_color="white",
                              fg_color="#226D68",
                              hover_color="#18534F",
                              bg_color="white",
                              height=30).place(x=400,y=5)
        tous= CTkButton(master=rech_frame, 
                        command=self.afficher,
                        text="Tous",
                        text_color="black",
                        fg_color="#FEEAA1",
                        hover_color="#D6955B",
                        bg_color="white",
                        width=25).place(x=545,y=5)

        #### liste produit

        listeFrame=Frame(self.root,bd=3,relief=RIDGE)
        listeFrame.place(x=680,y=120,height=630,width=800)

        scroll_y=Scrollbar(listeFrame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=Scrollbar(listeFrame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)

        self.produitliste=ttk.Treeview(listeFrame,columns=("pid","Catégorie","Fournisseur","Nom","Prix","Quantité","Statut"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
    
        scroll_x.config(command=self.produitliste.xview)
        scroll_y.config(command=self.produitliste.yview)

        self.produitliste.heading("pid",text="pid")
        self.produitliste.heading("Catégorie",text="Catégorie")
        self.produitliste.heading("Fournisseur",text="Fournisseur")
        self.produitliste.heading("Nom",text="Nom")
        self.produitliste.heading("Prix",text="Prix")
        self.produitliste.heading("Quantité",text="Quantité")
        self.produitliste.heading("Statut",text="Statut")

        self.produitliste["show"]="headings"

        self.produitliste.pack(fill=BOTH,expand=1)

        self.produitliste.bind("<ButtonRelease-1>",self.get_donnes)

        self.afficher()


    ###les fonction

    def liste_fou(self):
        self.four_liste.append("vide")
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()
        try:
            cur.execute("select nom from fournisseur")
            four=cur.fetchall()
            if len(four)>0:
                del self.four_liste[:]
                self.four_liste.append("Select")
                for i in four :
                    self.four_liste.append(i[0])



        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}")  

    def ajouter(self):
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_four.get()=="Select" or self.var_nom.get()=="":
                messagebox.showerror("Erreur", "Veillez saisir les champs obligatoires")
            else :
                cur.execute("select * from produit where nom=?",(self.var_nom.get(),))    
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Erreur", "Le produit existe déja")
                else:
                    cur.execute("insert into produit(categorie ,fournisseur ,nom ,prix ,quantite ,statut ) values(?,?,?,?,?,?)",
                                (self.var_cat.get(),
                                 self.var_four.get(),
                                 self.var_nom.get(),
                                 self.var_prix.get(),
                                 self.var_qte.get(),
                                 self.var_satut.get(),
                                ))
                    con.commit()
                    self.afficher()
                    self.rein()
                    messagebox.showinfo("Succés","Ajout effectué avec succés")

        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}") 

    def afficher(self):
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()
        try:
            cur.execute("select * from produit")
            rows = cur.fetchall()
            self.produitliste.delete(*self.produitliste.get_children())
            for row in rows:
                self.produitliste.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}")  
    
    def get_donnes(self,ev):
        self.btn_ajouter.configure(state="disabled")
        self.supprimer_btn.configure(state="normal")
        self.modifier_btn.configure(state="normal")
        r=self.produitliste.focus()
        contenu=self.produitliste.item(r)
        row=contenu["values"]  
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_four.set(row[2])
        self.var_nom.set(row[3])
        self.var_prix.set(row[4])
        self.var_qte.set(row[5])
        self.var_satut.set(row[6])

    def modifier(self):   
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Erreur","Selectionner un ID")
            else :
                cur.execute("select * from produit where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Erreur","Veillez selectionnez un produit sur la liste")
                else :
                    cur.execute("update produit set categorie=? ,fournisseur=? ,nom=?,prix=? ,quantite=? ,statut=? where pid=? ",(self.var_cat.get(),self.var_four.get(),self.var_nom.get(),self.var_prix.get(),self.var_qte.get(),self.var_satut.get(),self.var_pid.get()))
                    con.commit()
                    self.afficher()
                    self.rein()
                    messagebox.showinfo("Succés","Modification effectuée")


        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}") 

    def supprimer(self):
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()

        try:
            op=messagebox.askyesno("Confirmer","Voulez-vous vraiment supprimer?")
            if op==True:
                cur.execute("delete from produit where pid=?",(self.var_pid.get(),))
                con.commit()
                self.afficher()
                messagebox.showinfo("Succés","Suppression effectuée")

        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}") 

    def rein(self):
                                 self.var_pid.set("")
                                 self.var_cat.set("Select")
                                 self.var_four.set("Select")
                                 self.var_nom.set("")
                                 self.var_prix.set("")
                                 self.var_qte.set("")
                                 self.var_satut.set("Active")
                                 self.btn_ajouter.configure(state="normal")   
                                 self.modifier_btn.configure(state="disabled") 
                                 self.supprimer_btn.configure(state="disabled")
                                 self.var_recherche_txt.set("")

    def recherche(self):
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()

        try:
             
             if self.var_recherche_txt.get()=="":
                  messagebox.showerror("Erreur","Veillez saisir dans le champ de recherche")
             else :
                  cur.execute("select * from produit where "+self.var_recherche_type.get()+" like'%"+self.var_recherche_txt.get()+"%'")  
                  rows=cur.fetchall()
                  if len(rows)!=0 :
                       self.produitliste.delete(*self.produitliste.get_children())   
                       for row in rows :
                            self.produitliste.insert("",END,values=row)
                  else :
                       messagebox.showerror("Erreur","Aucun resultat trouvé")          
             

         
        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}")  


     







  






if __name__ == "__main__":
    root = CTk()
    obj = Produit(root)
    root.mainloop()
