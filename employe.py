from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox, ttk
import time
from customtkinter import *
import sqlite3

class Employe:
    def __init__(self, root):
        self.root = root
        self.root.title("Employe")
        self.root.geometry("1200x600+400+200")
        self.root.config(bg="white")
        self.root.focus_force()

        #connexion

        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS employe(ID text PRIMARY KEY,Nom text,Email text,Sexe text,Contact text,Naissance text,Adhésion text,Password text,Type text,Adresse text,Salaire text)")
        con.commit()

        ###les variables

        self.var_rchercher_type=StringVar()
        self.var_rchercher_txt=StringVar()
        self.var_emplo_id=StringVar()
        self.var_sexe=StringVar()
        self.var_contact=StringVar()
        self.var_nom=StringVar()
        self.var_naissance=StringVar()
        self.var_adhesion=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_type=StringVar()
        self.var_salaire=StringVar()


        #frame rechercher

        reche_Frame=LabelFrame(self.root,
                               text="Rechercher Employé",
                               font=("goudy old style",20,"bold"),
                               bd=2,
                               relief=RIDGE,bg="white")
        reche_Frame.place(x=400,y=20,width=750,height=90)

        #option de recherche

        reche_option=ttk.Combobox(reche_Frame,
                                  textvariable=self.var_rchercher_type,
                                  values=("Nom","Prenom","Email","Contact"),
                                  font=("times new roman",20),
                                  state="r",
                                  justify=CENTER)
        reche_option.current(0) #ou bien set("selectionne")
        reche_option.place(x=10,y=10,width=200)

        reche_text=Entry(reche_Frame,
                         textvariable=self.var_rchercher_txt,
                         font=("times new roman",20),
                         bg="lightyellow").place(x=235,y=10,width=200)

        recherche= CTkButton(master=reche_Frame,
                              text="Rechercher",
                              text_color="white",
                              fg_color="#226D68",
                              hover_color="#18534F",
                              bg_color="white").place(x=360,y=5)
        tous= CTkButton(master=reche_Frame, 
                        command=self.afficher,
                        text="Tous",
                        text_color="black",
                        fg_color="#FEEAA1",
                        hover_color="#D6955B",
                        bg_color="white",
                        width=25).place(x=510,y=5)
        
        #titre

        titre=Label(self.root,
                    text="Formulaire Employé",
                    font=("times new roman",20),
                    cursor="hand2",
                    bg="#76CDCD").place(x=0,y=150,width=1499)
        
        #####contenu

        #ligne1

        lbl_empid=Label(self.root,
                        text="ID Employé",
                        font=("goudy old style",20),
                        bg="white").place(x=50,y=220,width=200) 
        lbl_sexe=Label(self.root,
                       text="Sexe",
                       font=("goudy old style",20),
                       bg="white").place(x=500,y=220,width=200) 
        lbl_contact=Label(self.root,
                          text="Contact",
                          font=("goudy old style",20),
                          bg="white").place(x=900,y=220,width=200) 

        self.txt_empid=Entry(self.root,
                        textvariable=self.var_emplo_id,
                        font=("goudy old style",20),
                        bg="lightyellow")
        self.txt_empid.place(x=250,y=220,width=250)
        txt_sexe=ttk.Combobox(self.root,
                        textvariable=self.var_sexe,
                        values=("Homme","Femme"),
                        state="r",
                        justify=CENTER,       
                        font=("goudy old style",20))
        txt_sexe.current(0)
        txt_sexe.place(x=680,y=220,width=250)
        txt_contact=Entry(self.root,
                        textvariable=self.var_contact,
                        font=("goudy old style",20),
                        bg="lightyellow").place(x=1100,y=220,width=250)
        
         #ligne2

        lbl_nom=Label(self.root,
                        text="Nom",
                        font=("goudy old style",20),
                        bg="white").place(x=50,y=290,width=200) 
        lbl_naissance=Label(self.root,
                       text="Date de naissance",
                       font=("goudy old style",18),
                       bg="white").place(x=486,y=290,width=200) 
        lbl_adehsion=Label(self.root,
                          text="Date d'adhésion",
                          font=("goudy old style",18),
                          bg="white").place(x=914,y=290,width=200) 
        

        txt_nom=Entry(self.root,
                        textvariable=self.var_nom,
                        font=("goudy old style",20),
                        bg="lightyellow").place(x=250,y=290,width=250)
        txt_naissance=Entry(self.root,
                        textvariable=self.var_naissance,    
                        font=("goudy old style",20),
                        bg="lightyellow").place(x=680,y=290,width=250)
        txt_adhesion=Entry(self.root,
                        textvariable=self.var_adhesion,
                        font=("goudy old style",20),
                        bg="lightyellow").place(x=1100,y=290,width=250)
         #ligne3

        lbl_email=Label(self.root,
                        text="Email",
                        font=("goudy old style",20),
                        bg="white").place(x=50,y=360,width=200) 
        lbl_password=Label(self.root,
                       text="Password",
                       font=("goudy old style",20),
                       bg="white").place(x=486,y=360,width=200) 
        lbl_type=Label(self.root,
                          text="Type",
                          font=("goudy old style",20),
                          bg="white").place(x=914,y=360,width=200) 
        

        txt_email=Entry(self.root,
                        textvariable=self.var_email,
                        font=("goudy old style",20),
                        bg="lightyellow").place(x=250,y=360,width=250)
        txt_password=Entry(self.root,
                        textvariable=self.var_password,   
                        show="*",
                        font=("goudy old style",20),
                        bg="lightyellow").place(x=680,y=360,width=250)
        txt_type=ttk.Combobox(self.root,
                        textvariable=self.var_type,      
                        values=("Admin","Employé"),
                        state="r",
                        justify=CENTER,       
                        font=("goudy old style",20))
        txt_type.current(0)
        txt_type.place(x=1100,y=360,width=250)   

         #ligne4

        lbl_adresse=Label(self.root,
                        text="Adresse",
                        font=("goudy old style",20),
                        bg="white").place(x=50,y=430,width=200) 
        lbl_salaire=Label(self.root,
                       text="Salaire",
                       font=("goudy old style",20),
                       bg="white").place(x=486,y=430,width=200) 

        

        self.txt_adresse=Text(self.root,
                        font=("goudy old style",20),
                        bg="lightyellow")
        self.txt_adresse.place(x=250,y=430,width=250,height=115)
        txt_salaire=Entry(self.root,
                        textvariable=self.var_salaire,
                        font=("goudy old style",20),
                        bg="lightyellow").place(x=680,y=430,width=250)
        

        #button

        self.ajout_btn = CTkButton(master=self.root,
                                    state="normal",
                                    command=self.ajouter,
                                    text="Ajouter",
                                    font=("times new roman",20,"bold"),
                                    text_color="black",
                                    corner_radius=32,
                                    hover_color="#679436",
                                    fg_color="#8FB43A",
                                    bg_color="white",
                                    height=40) 
        self.ajout_btn.place(x=420,y=390)
        self.modifier_btn = CTkButton(master=self.root,
                                    state="disabled",
                                    text="Modifier",
                                    font=("times new roman",20,"bold"),
                                    text_color="black",
                                    corner_radius=32,
                                    hover_color="#EBBD04",
                                    fg_color="#FEE552",
                                    bg_color="white",
                                    height=40) 
        self.modifier_btn.place(x=600,y=390)
        self.supprimer_btn = CTkButton(master=self.root,
                                    state="disabled",   
                                    text="Supprimer",
                                    font=("times new roman",20,"bold"),
                                    text_color="black",
                                    corner_radius=32,
                                    hover_color="#A92831",
                                    fg_color="#CF4146", 
                                    bg_color="white",
                                    height=40) 
        self.supprimer_btn.place(x=780,y=390)
        reni_btn = CTkButton(master=self.root,
                                    text="Reinitialiser",
                                    font=("times new roman",20,"bold"),
                                    text_color="black",
                                    corner_radius=32,
                                    hover_color="#D5CD90",
                                    fg_color="#EEEACB",
                                    bg_color="white",
                                    height=40) 
        reni_btn.place(x=960,y=390)

        ###liste Employe

        listeFrame=Frame(self.root,bd=3,relief=RIDGE)
        listeFrame.place(x=0,y=550,height=206,relwidth=1)

        scroll_y=Scrollbar(listeFrame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=Scrollbar(listeFrame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)

        self.employelist=ttk.Treeview(listeFrame,columns=("ID",
                                                          "Nom",
                                                          "Email",
                                                          "Sexe",
                                                          "Contact",
                                                          "Naissance",
                                                          "Adhésion",
                                                          "Password",
                                                          "Type",
                                                          "Adresse",
                                                          "Salaire"),
                                                          yscrollcommand=scroll_y.set,
                                                          xscrollcommand=scroll_x.set)
        
        scroll_x.config(command=self.employelist.xview)
        scroll_y.config(command=self.employelist.yview)

        self.employelist.heading("ID",text="ID")
        self.employelist.heading("Nom",text="Nom")
        self.employelist.heading("Email",text="Email")
        self.employelist.heading("Sexe",text="Sexe")
        self.employelist.heading("Contact",text="Contact")
        self.employelist.heading("Naissance",text="Naissance")
        self.employelist.heading("Adhésion",text="Adhésion")
        self.employelist.heading("Password",text="Password")
        self.employelist.heading("Type",text="Type")
        self.employelist.heading("Adresse",text="Adresse")
        self.employelist.heading("Salaire",text="Salaire")

        self.employelist["show"]="headings"

        self.employelist.bind("<ButtonRelease-1>",self.get_donnes)



        self.employelist.pack(fill=BOTH,expand=1)

        self.afficher()
    ###fonction

    def ajouter(self):
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()
        try:
            if self.var_emplo_id.get()=="" or self.var_password.get()=="" or self.var_type.get()=="" :
                messagebox.showerror("Erreur", "Veuillez mettre un ID, password et type")
            else :
                cur.execute("select * from employe where ID=?",(self.var_emplo_id.get(),))    
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Erreur", "L'ID de l'employé existe déja")
                else:
                    cur.execute("insert into employe(ID ,Nom ,Email ,Sexe ,Contact ,Naissance ,Adhésion ,Password ,Type ,Adresse ,Salaire ) values(?,?,?,?,?,?,?,?,?,?,?)",
                                (self.var_emplo_id.get(),
                                 self.var_nom.get(),
                                 self.var_email.get(),
                                 self.var_sexe.get(),
                                 self.var_contact.get(),
                                 self.var_naissance.get(),
                                 self.var_adhesion.get(),
                                 self.var_password.get(),
                                 self.var_type.get(),
                                 self.txt_adresse.get("1.0",END),
                                 self.var_salaire.get()))
                    con.commit()
                    self.afficher()
                    messagebox.showinfo("Succés","Ajout effectué avec succés")

        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}")   
 
    def afficher(self):
        con=sqlite3.connect(database=r"C:\Users\abdou\Desktop\Gestion_de_stock_et_caisse_enregistreuse\Données\magasinbase.db")
        cur=con.cursor()
        try:
            cur.execute("select * from employe")
            rows = cur.fetchall()
            self.employelist.delete(*self.employelist.get_children())
            for row in rows:
                self.employelist.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Erreur",f"Erreur de connexion {str(ex)}")  

    def get_donnes(self,ev):
        self.ajout_btn.configure(state="disabled")
        self.supprimer_btn.configure(state="normal")
        self.modifier_btn.configure(state="normal")

        self.txt_empid.config(state="readonly")    
        r=self.employelist.focus()
        contenu=self.employelist.item(r)
        row=contenu["values"]  

        self.var_emplo_id.set(row[0]),
        self.var_nom.set(row[1]),
        self.var_email.set(row[2]),
        self.var_sexe.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_naissance.set(row[5]),
        self.var_adhesion.set(row[6]),
        self.var_password.set(row[7]),
        self.var_type.set(row[8]),
        self.txt_adresse.delete("1.0",END),
        self.txt_adresse.insert(END,row[9])
        self.var_salaire.set(row[10])










if __name__ == "__main__":
    root = CTk()
    obj = Employe(root)
    root.mainloop()
