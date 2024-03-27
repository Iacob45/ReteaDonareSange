import customtkinter
import mysql.connector
from PIL import Image, ImageTk

class Aplicatie:

    def __init__(self,username="",parola=""):
        self.username = username
        self.parola = parola


    def login(self, frame, root, entry1, entry2):
        self.username = entry1.get()
        self.parola = entry2.get()

        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="a2mEfc@#uo%*cQ",database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        SELECT COUNT(username) FROM users
        WHERE username = '{}'
        """.format(self.username))


        if(self.cursor.fetchall()[0][0] != 0):
            self.cursor.execute("""
            SELECT * FROM users
            WHERE username = '{}'
            """.format(self.username))
            results = self.cursor.fetchone()
            self.connection.close()

            if(results[2] != ''):
                if(results[2] == self.parola):
                    u = User()
                    u.load_user(self.username)
                    self.start2(root, frame, u)
                else:
                    eroare = customtkinter.CTkLabel(master=frame, width=400, height=80, text="Date incorecte", text_color=("Red"),font=("Roboto", 14))
                    eroare.pack(pady=12, padx=10)
                    eroare.place(relx=0.5, rely=0.6, anchor='center')
            else:
                eroare = customtkinter.CTkLabel(master=frame, width=400, height=80, text="Date incorecte", text_color=("Red"),font=("Roboto", 14))
                eroare.pack(pady=12, padx=10)
                eroare.place(relx=0.5, rely=0.6, anchor='center')
        else:
            eroare = customtkinter.CTkLabel(master=frame, width=400, height=80, text="Date incorecte", text_color=("Red"),font=("Roboto", 14))
            eroare.pack(pady=12, padx=10)
            eroare.place(relx=0.5, rely=0.6, anchor='center')
            self.connection.close()


    def register_user(self, frame, root):

        frame.destroy()

        customtkinter.set_default_color_theme("green")
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Inregistrare cont nou", font=("Roboto", 24))
        label.pack(pady=32, padx=10)

        entry1 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Username")
        entry1.pack(pady=12, padx=10)
        entry1.place(relx=0.1, rely=0.28, anchor='w')
        entry2 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Parola", show="*")
        entry2.pack(pady=12, padx=10)
        entry2.place(relx=0.1, rely=0.34, anchor='w')
        entry3 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Grupa de sange")
        entry3.pack(pady=12, padx=10)
        entry3.place(relx=0.1, rely=0.4, anchor='w')
        entry4 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Nume")
        entry4.pack(pady=12, padx=10)
        entry4.place(relx=0.1, rely=0.46, anchor='w')
        entry5 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Prenume")
        entry5.pack(pady=12, padx=10)
        entry5.place(relx=0.1, rely=0.52, anchor='w')
        entry6 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Email")
        entry6.pack(pady=12, padx=10)
        entry6.place(relx=0.1, rely=0.58, anchor='w')
        entry7 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Telefon")
        entry7.pack(pady=12, padx=10)
        entry7.place(relx=0.1, rely=0.64, anchor='w')
        entry8 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Oras")
        entry8.pack(pady=12, padx=10)
        entry8.place(relx=0.1, rely=0.7, anchor='w')
        entry9 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Adresa")
        entry9.pack(pady=12, padx=10)
        entry9.place(relx=0.1, rely=0.76, anchor='w')

        button_register = customtkinter.CTkButton(master=frame, width=200, text_color=("white"),font=("Roboto", 24), height=50, text="Inregistrare",command=lambda: self.verify_register(frame, root, entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get(), entry7.get(), entry8.get(), entry9.get()))
        button_register.pack(pady=12, padx=10)
        button_register.place(relx=0.5, rely=0.86, anchor='center')

        back_img = customtkinter.CTkImage(Image.open("assets/backarrow.png"), size=(30, 30))
        back_button = customtkinter.CTkButton(master=frame, width=66, height=26, text="", image=back_img,
                                              fg_color="Green", hover_color="#FC6C85",
                                              command=lambda: self.start(root, frame))
        back_button.pack()
        back_button.place(relx=0.07, rely=0.12, anchor='w')

    def verify_register(self, frame, root, e1, e2, e3, e4, e5, e6, e7, e8, e9):
        if(e1 != "" and e2 != "" and e3 != "" and e4 != "" and e5 != "" and e6 != "" and e7 != "" and e8 != "" and e9 != ""):
            self.connection = mysql.connector.connect(host="localhost", user="root", passwd="a2mEfc@#uo%*cQ",database="reteadonaresange")
            self.cursor = self.connection.cursor()
            self.cursor.execute("""
                        SELECT COUNT(username) FROM users
                        WHERE username = '{}'
                        """.format(e1))
            if (self.cursor.fetchall()[0][0] != 0):
                eroare = customtkinter.CTkLabel(master=frame, width=400, height=30,
                                                        text="Un cont cu acelasi username deja exista",
                                                        text_color=("Brown"), font=("Roboto", 20))
                eroare.pack(pady=12, padx=10)
                eroare.place(relx=0.7, rely=0.75, anchor='center')
            else:
                u = User()
                u.username = e1
                u.parola = e2
                u.grupasange = e3
                u.nume = e4
                u.prenume = e5
                u.email = e6
                u.telefon = e7
                u.oras = e8
                u.adresa = e9
                u.insert_user()

                self.start2(root, frame, u)
        else:
            eroare = customtkinter.CTkLabel(master=frame, width=400, height=30, text="Nu toate campurile au fost completate",text_color=("Red"), font=("Roboto", 20))
            eroare.pack(pady=12, padx=10)
            eroare.place(relx=0.7, rely=0.75, anchor='center')





    def start(self, root=None, frame=None):
        if(frame != None):
            frame.destroy()
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("dark-blue")


        if(root == None):
            root = customtkinter.CTk()
            root.geometry("1000x600")

        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Autentificare", font=("Roboto", 24))
        label.pack(pady=32, padx=10)

        entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="ID utilizator")
        entry1.pack(pady=12, padx=10)
        entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Parola", show="*")
        entry2.pack(pady=12, padx=10)


        button_login = customtkinter.CTkButton(master=frame, text="Autentificare", command= lambda: self.login(frame,root,entry1,entry2))
        button_login.pack(pady=12, padx=10)

        button_register = customtkinter.CTkButton(master=frame, text="Inregistrare", command=lambda: self.register_user(frame, root))
        button_register.pack(pady=12, padx=10)

        root.mainloop()

    def start2(self, root, frame, u):
        frame.destroy()
        customtkinter.set_default_color_theme("green")
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        button1 = customtkinter.CTkButton(master=frame, width=400, height=100, fg_color="#FF66CC", hover_color="#FFC1CC", font=("Roboto", 33), text="Donator",command=lambda: self.appdonator(frame, root, u))
        button1.pack(pady=12, padx=10)
        button1.place(relx=0.5, rely=0.3, anchor='center')

        button2 = customtkinter.CTkButton(master=frame, width=400, height=100, fg_color="#77C3EC", hover_color="#446CCF", font=("Roboto", 33), text="Beneficiar",command=lambda: self.appbeneficiar(frame, root, u))
        button2.pack(pady=12, padx=10)
        button2.place(relx=0.5, rely=0.55, anchor='center')

        logout_img = customtkinter.CTkImage(Image.open("assets/logout.png"), size=(30, 30))
        logout_button = customtkinter.CTkButton(master=frame, width=46, height=51, text="", image=logout_img,
                                              fg_color="#333333", hover_color="#373737",
                                              command=lambda: self.start(root, frame))
        logout_button.pack()
        logout_button.place(relx=0.07, rely=0.12, anchor='w')

    def appdonator(self, frame, root, u):
        app = 0
        frame.destroy()
        customtkinter.set_default_color_theme("green")
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        button1 = customtkinter.CTkButton(master=frame, width=300, height=60, fg_color="#FF66CC", hover_color="#FF007F", font=("Roboto", 25),
                                          text="Centre disponibile",
                                          command=lambda: self.centre_disponibile(frame, root, u, app))
        button1.pack(pady=12, padx=10)
        button1.place(relx=0.3, rely=0.3, anchor='center')

        button2 = customtkinter.CTkButton(master=frame, width=300, height=60, fg_color="#FF66CC", hover_color="#FF007F", font=("Roboto", 25),
                                          text="Inregistrare programare",
                                          command=lambda: self.inregistrare_programare(frame, root, u, app))
        button2.pack(pady=12, padx=10)
        button2.place(relx=0.3, rely=0.42, anchor='center')

        button3 = customtkinter.CTkButton(master=frame, width=300, height=60, fg_color="#FF66CC", hover_color="#FF007F", font=("Roboto", 25),
                                          text="Viuzalizare programari",
                                          command=lambda: self.vizualizare_programari(frame, root, u, app))
        button3.pack(pady=12, padx=10)
        button3.place(relx=0.3, rely=0.54, anchor='center')

        button4 = customtkinter.CTkButton(master=frame, width=300, height=60, fg_color="#FF66CC", hover_color="#FF007F", font=("Roboto", 25),
                                          text="Istoric donari",
                                          command=lambda: self.istoric_donari(frame, root, u, app))
        button4.pack(pady=12, padx=10)
        button4.place(relx=0.3, rely=0.66, anchor='center')


        profile_img = customtkinter.CTkImage(Image.open("assets/profilepic.webp"), size=(30, 30))
        profile_button = customtkinter.CTkButton(master=frame, width=66, height=46, text="", image=profile_img,
                                                fg_color="#FC0FC0", hover_color="#E0115F", command=lambda: self.edit_profil(frame, root, u, app))
        profile_button.pack()
        profile_button.place(relx=0.9, rely=0.084, anchor='w')

        back_img = customtkinter.CTkImage(Image.open("assets/backarrow.png"), size=(30, 30))
        back_button = customtkinter.CTkButton(master=frame, width=66, height=26, text="", image=back_img,
                                              fg_color="#FC8EAC", hover_color="#FC6C85",
                                              command=lambda: self.start2(root, frame, u))
        back_button.pack()
        back_button.place(relx=0.07, rely=0.12, anchor='w')


    def appbeneficiar(self, frame, root, u):
        app = 1
        frame.destroy()
        customtkinter.set_default_color_theme("green")
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        button1 = customtkinter.CTkButton(master=frame, width=300, height=60, fg_color="#1E90FF", hover_color="#1560BD", font=("Roboto", 25),
                                          text="Centre disponibile",
                                          command=lambda: self.centre_disponibile(frame, root, u, app))
        button1.pack(pady=12, padx=10)
        button1.place(relx=0.3, rely=0.3, anchor='center')

        button2 = customtkinter.CTkButton(master=frame, width=300, height=60, fg_color="#1E90FF", hover_color="#1560BD", font=("Roboto", 25),
                                          text="Inregistrare programare",
                                          command=lambda: self.inregistrare_programare(frame, root, u, app))
        button2.pack(pady=12, padx=10)
        button2.place(relx=0.3, rely=0.42, anchor='center')

        button3 = customtkinter.CTkButton(master=frame, width=300, height=60, fg_color="#1E90FF", hover_color="#1560BD", font=("Roboto", 25),
                                          text="Viuzalizare programari",
                                          command=lambda: self.vizualizare_programari(frame, root, u, app))
        button3.pack(pady=12, padx=10)
        button3.place(relx=0.3, rely=0.54, anchor='center')

        button4 = customtkinter.CTkButton(master=frame, width=300, height=60, fg_color="#1E90FF", hover_color="#1560BD", font=("Roboto", 25),
                                          text="Istoric donari",
                                          command=lambda: self.istoric_donari(frame, root, u, app))
        button4.pack(pady=12, padx=10)
        button4.place(relx=0.3, rely=0.66, anchor='center')

        button5 = customtkinter.CTkButton(master=frame, width=300, height=60, fg_color="#1E90FF", hover_color="#1560BD", font=("Roboto", 25),
                                          text="Donatori potentiali",
                                          command=lambda: self.donatori_potentiali(frame, root, u, app))
        button5.pack(pady=12, padx=10)
        button5.place(relx=0.3, rely=0.78, anchor='center')

        profile_img = customtkinter.CTkImage(Image.open("assets/profilepic.webp"), size=(30, 30))
        profile_button = customtkinter.CTkButton(master=frame, width=66, height=46, text="", image=profile_img,
                                                fg_color="#1560BD", hover_color="#032174", command=lambda: self.edit_profil(frame, root, u, app))
        profile_button.pack()
        profile_button.place(relx=0.9, rely=0.084, anchor='w')

        back_img = customtkinter.CTkImage(Image.open("assets/backarrow.png"), size=(30, 30))
        back_button = customtkinter.CTkButton(master=frame, width=66, height=26, text="", image=back_img,
                                              fg_color="#4169E1", hover_color="#90E0EF",
                                              command=lambda: self.start2(root, frame, u))
        back_button.pack()
        back_button.place(relx=0.07, rely=0.12, anchor='w')


    def donatori_potentiali(self, frame, root, u, app):
        frame.destroy()
        customtkinter.set_default_color_theme("blue")
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text="Donatori potentiali din " + u.oras, font=("Roboto", 24))
        label.pack(pady=45, padx=10)

        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="a2mEfc@#uo%*cQ",
                                                  database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
                                        SELECT id_cont FROM users
                                        """)
        results = [row[0] for row in self.cursor.fetchall()]
        donatori = []

        for x in results:
            d = User()
            d.load_user("",x)
            donatori.append(d)

        for x in donatori:
            if x.oras == u.oras and x.id_cont != u.id_cont:

                label = customtkinter.CTkLabel(master=frame, font=("Roboto", 17, "italic"), text_color="#3F3F4E",
                                               text="Nume: {}, Prenume: {}, Telefon: {}".format(
                                                   x.nume, x.prenume, x.telefon))
                label.pack(pady=0, padx=0)


        back_img = customtkinter.CTkImage(Image.open("assets/backarrow.png"), size=(30, 30))
        back_button = customtkinter.CTkButton(master=frame, width=66, height=26, text="", image=back_img,
                                              fg_color="#00A86B", hover_color="#3F704D",
                                              command=lambda: self.back_select(frame, root, u, app))
        back_button.pack()
        back_button.place(relx=0.07, rely=0.12, anchor='w')


    def istoric_donari(self, frame, root, u, app):
        frame.destroy()
        customtkinter.set_default_color_theme("blue")
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text="Istoric donari", font=("Roboto", 24))
        label.pack(pady=45, padx=10)

        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="a2mEfc@#uo%*cQ",
                                                  database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
                                SELECT id_donare FROM istoricdonari
                                """)
        results = [row[0] for row in self.cursor.fetchall()]
        donari = []

        for x in results:
            d = Istoricdonari()
            d.load_istoricdonare(x)
            donari.append(d)

        for x in donari:
            if x.id_donator == u.id_cont or x.id_beneficiar == u.id_cont:
                ud = User()
                ud.load_user("", x.id_donator)
                ub = User()
                ub.load_user("", x.id_beneficiar)
                c = Centru()
                c.load_centru(x.id_centru)

                label = customtkinter.CTkLabel(master=frame, font=("Roboto", 17, "italic"), text_color="#3F3F4E",
                                               text="Donator: {}, Beneficiar: {}, Centru: {}, Data: {}, Ora: {}".format(
                                                   ud.prenume, ub.prenume, c.nume, x.data, x.ora))
                label.pack(pady=0, padx=0)

                if(app == 1):
                    label = customtkinter.CTkLabel(master=frame, font=("Roboto", 17, "italic"), text_color="#3F3F4E",
                                                   text="Feedback beneficiar:")
                    label.pack(pady=0, padx=0)
                    entry = customtkinter.CTkEntry(master=frame, placeholder_text="Feedback beneficiar")
                    entry.insert(0,x.feedbackbeneficiar)
                    entry.pack(pady=12, padx=10)
                elif(app == 0):
                    label = customtkinter.CTkLabel(master=frame, font=("Roboto", 17, "italic"), text_color="#3F3F4E",
                                                   text="Feedback beneficiar: " + x.feedbackbeneficiar)
                    label.pack(pady=6, padx=0)

        back_img = customtkinter.CTkImage(Image.open("assets/backarrow.png"), size=(30, 30))
        back_button = customtkinter.CTkButton(master=frame, width=66, height=26, text="", image=back_img,
                                              fg_color="#00A86B", hover_color="#3F704D",
                                              command=lambda: self.back_select(frame, root, u, app))
        back_button.pack()
        back_button.place(relx=0.07, rely=0.12, anchor='w')


    def vizualizare_programari(self, frame, root, u, app):
        frame.destroy()
        customtkinter.set_default_color_theme("blue")
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text="Programari personale", font=("Roboto", 24))
        label.pack(pady=45, padx=10)



        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="a2mEfc@#uo%*cQ",
                                                  database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
                        SELECT id_programare FROM programari
                        """)
        results = [row[0] for row in self.cursor.fetchall()]
        programari = []

        for x in results:
            p = Programari()
            p.load_programare(x)
            programari.append(p)


        for x in programari:
            if x.id_donator == u.id_cont or x.id_beneficiar == u.id_cont:
                ud = User()
                ud.load_user("",x.id_donator)
                ub = User()
                ub.load_user("",x.id_beneficiar)
                c = Centru()
                c.load_centru(x.id_centru)

                label = customtkinter.CTkLabel(master=frame, font=("Roboto",17,"italic"), text_color="#3F3F4E", text="Donator: {}, Beneficiar: {}, Centru: {}, Data: {}, Ora: {}".format(ud.prenume, ub.prenume, c.nume, x.data, x.ora))
                label.pack(pady=6, padx=0)

        back_img = customtkinter.CTkImage(Image.open("assets/backarrow.png"), size=(30, 30))
        back_button = customtkinter.CTkButton(master=frame, width=66, height=26, text="", image=back_img,
                                              fg_color="#00A86B", hover_color="#3F704D",
                                              command=lambda: self.back_select(frame, root, u, app))
        back_button.pack()
        back_button.place(relx=0.07, rely=0.12, anchor='w')


    def centre_disponibile(self, frame, root, u, app):
        frame.destroy()
        customtkinter.set_default_color_theme("blue")
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.connection = mysql.connector.connect(host="localhost", user="root", passwd="a2mEfc@#uo%*cQ",
                                                  database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
                SELECT id_centru FROM centredonare
                """)
        results = [row[0] for row in self.cursor.fetchall()]
        centre = []

        for x in results:
            c = Centru()
            c.load_centru(x)
            centre.append(c)

        self.cursor.execute("""
                            SELECT COUNT(id_centru) FROM centredonare
                            WHERE oras = '{}'
                            """.format(u.oras))

        i = 0
        if (self.cursor.fetchall()[0][0] != 0):
            label = customtkinter.CTkLabel(master=frame, text="Centre din " + u.oras, font=("Roboto", 24))
            label.pack(pady=32, padx=10)
            label.place(relx=0.4, rely=0.1, anchor='center')

            for x in centre:
                if x.oras == u.oras:
                    button_centru = customtkinter.CTkButton(master=frame, fg_color='#BF0A30', hover_color='#BF0A30',
                                                            text="Oras: {}\nAdresa: {}\nTelefon: {}\nStoc sange: {}".format(x.oras, x.adresa,
                                                                                             x.telefon, x.stocsange))
                    button_centru.pack(pady=12, padx=10)
                    button_centru.place(relx=0.4, rely=0.34 + 0.26 * i, anchor='center')
                    button_centru = customtkinter.CTkButton(master=frame, width=400, height=50, fg_color='#BF0A30',
                                                            hover_color='#BF0A30', text=x.nume, font=("Roboto", 20))
                    button_centru.pack(pady=12, padx=10)
                    button_centru.place(relx=0.4, rely=0.24 + 0.26 * i, anchor='center')
                    i = i + 1
            i = i + 0.5

        label2 = customtkinter.CTkLabel(master=frame, text="Centre din Romania", font=("Roboto", 24))
        label2.pack(pady=32, padx=10)
        label2.place(relx=0.4, rely=0.1 + 0.26 * i, anchor='center')


        for x in centre:
            if x.oras != u.oras:
                button_centru = customtkinter.CTkButton(master=frame, fg_color='#BF0A30', hover_color='#BF0A30',
                                                        text="Oras: {}\nAdresa: {}\nTelefon: {}\nStoc sange: {}".format(x.oras, x.adresa,
                                                                                         x.telefon, x.stocsange))
                button_centru.pack(pady=12, padx=10)
                button_centru.place(relx=0.4, rely=0.34 + 0.26 * i, anchor='center')
                button_centru = customtkinter.CTkButton(master=frame, width=400, height=50, fg_color='#BF0A30',
                                                        hover_color='#BF0A30', text=x.nume, font=("Roboto", 20))
                button_centru.pack(pady=12, padx=10)
                button_centru.place(relx=0.4, rely=0.24 + 0.26 * i, anchor='center')
                i = i + 1

        back_img = customtkinter.CTkImage(Image.open("assets/backarrow.png"), size=(30, 30))
        back_button = customtkinter.CTkButton(master=frame, width=66, height=26, text="", image=back_img,
                                              fg_color="#00A86B", hover_color="#3F704D",
                                              command=lambda: self.back_select(frame, root, u, app))
        back_button.pack()
        back_button.place(relx=0.07, rely=0.12, anchor='w')

        self.connection.close()

    def inregistrare_programare(self, frame, root, u, app):
        if(app == 0):

            frame.destroy()
            customtkinter.set_default_color_theme("green")
            frame = customtkinter.CTkFrame(master=root)
            frame.pack(pady=20, padx=60, fill="both", expand=True)

            label = customtkinter.CTkLabel(master=frame, text="Inregistrare programare", font=("Roboto", 24))
            label.pack(pady=32, padx=10)

            observatie = customtkinter.CTkLabel(master=frame, text="*Pentru o donatie fara un anumit beneficiar puneti: -", font=("Roboto", 12))
            observatie.pack(pady=32, padx=10)
            observatie.place(relx=0.9, rely=0.18, anchor='e')

            label1 = customtkinter.CTkLabel(master=frame, text="Nume si prenume donator:")
            label1.pack(pady=12, padx=10)
            label1.place(relx=0.2, rely=0.28, anchor='e')
            label2 = customtkinter.CTkLabel(master=frame, text="Numar de telefon donator:")
            label2.pack(pady=12, padx=10)
            label2.place(relx=0.2, rely=0.34, anchor='e')
            label3 = customtkinter.CTkLabel(master=frame, text="Nume si prenume beneficiar:")
            label3.pack(pady=12, padx=10)
            label3.place(relx=0.2, rely=0.4, anchor='e')
            label4 = customtkinter.CTkLabel(master=frame, text="Numar de telefon beneficiar:")
            label4.pack(pady=12, padx=10)
            label4.place(relx=0.2, rely=0.46, anchor='e')
            label5 = customtkinter.CTkLabel(master=frame, text="Nume centru de donare:")
            label5.pack(pady=12, padx=10)
            label5.place(relx=0.2, rely=0.52, anchor='e')
            label6 = customtkinter.CTkLabel(master=frame, text="Data:")
            label6.pack(pady=12, padx=10)
            label6.place(relx=0.2, rely=0.58, anchor='e')
            label7 = customtkinter.CTkLabel(master=frame, text="Ora:")
            label7.pack(pady=12, padx=10)
            label7.place(relx=0.2, rely=0.64, anchor='e')
            entry1 = customtkinter.CTkLabel(master=frame, text=u.nume + " " + u.prenume)
            entry1.pack(pady=12, padx=10)
            entry1.place(relx=0.21, rely=0.28, anchor='w')
            entry2 = customtkinter.CTkLabel(master=frame, text=u.telefon)
            entry2.pack(pady=12, padx=10)
            entry2.place(relx=0.21, rely=0.34, anchor='w')
            entry3a = customtkinter.CTkEntry(master=frame, width=150, placeholder_text="Nume beneficiar")
            entry3a.pack(pady=12, padx=10)
            entry3a.place(relx=0.21, rely=0.4, anchor='w')
            entry3b = customtkinter.CTkEntry(master=frame, width=150, placeholder_text="Prenume beneficiar")
            entry3b.pack(pady=12, padx=10)
            entry3b.place(relx=0.38, rely=0.4, anchor='w')
            entry4 = customtkinter.CTkEntry(master=frame, width=300, placeholder_text="Numar de telefon beneficiar")
            entry4.pack(pady=12, padx=10)
            entry4.place(relx=0.21, rely=0.46, anchor='w')
            entry5 = customtkinter.CTkEntry(master=frame, width=300, placeholder_text="Nume centru de donare")
            entry5.pack(pady=12, padx=10)
            entry5.place(relx=0.21, rely=0.52, anchor='w')
            entry6 = customtkinter.CTkEntry(master=frame, width=300, placeholder_text="Data")
            entry6.pack(pady=12, padx=10)
            entry6.place(relx=0.21, rely=0.58, anchor='w')
            entry7 = customtkinter.CTkEntry(master=frame, width=300, placeholder_text="Ora")
            entry7.pack(pady=12, padx=10)
            entry7.place(relx=0.21, rely=0.64, anchor='w')


            button_programare = customtkinter.CTkButton(master=frame, width=200, text_color=("white"), font=("Roboto", 24),
                                                  height=50, text="Inscriere programare",
                                                  fg_color="#3BB143", hover_color="#0B6623",
                                                  command=lambda: self.inscriere_programare0(frame, root, u, app,
                                                                                     entry3a.get(), entry3b.get(),
                                                                                     entry4.get(), entry5.get(),
                                                                                     entry6.get(), entry7.get()))
            button_programare.pack(pady=12, padx=10)
            button_programare.place(relx=0.5, rely=0.86, anchor='center')

            back_img = customtkinter.CTkImage(Image.open("assets/backarrow.png"), size=(30, 30))
            back_button = customtkinter.CTkButton(master=frame, width=66, height=26, text="", image=back_img,
                                                  fg_color="#00A86B", hover_color="#3F704D",
                                                  command=lambda: self.back_select(frame, root, u, app))
            back_button.pack()
            back_button.place(relx=0.07, rely=0.12, anchor='w')

        elif(app == 1):

            frame.destroy()
            customtkinter.set_default_color_theme("green")
            frame = customtkinter.CTkFrame(master=root)
            frame.pack(pady=20, padx=60, fill="both", expand=True)

            label = customtkinter.CTkLabel(master=frame, text="Inregistrare programare", font=("Roboto", 24))
            label.pack(pady=32, padx=10)

            observatie = customtkinter.CTkLabel(master=frame, text="*Pentru o donatie fara un anumit beneficiar puneti: -", font=("Roboto", 12))
            observatie.pack(pady=32, padx=10)
            observatie.place(relx=0.9, rely=0.18, anchor='e')

            label1 = customtkinter.CTkLabel(master=frame, text="Nume si prenume beneficiar:")
            label1.pack(pady=12, padx=10)
            label1.place(relx=0.2, rely=0.28, anchor='e')
            label2 = customtkinter.CTkLabel(master=frame, text="Numar de telefon beneficiar:")
            label2.pack(pady=12, padx=10)
            label2.place(relx=0.2, rely=0.34, anchor='e')
            label3 = customtkinter.CTkLabel(master=frame, text="Nume si prenume donator:")
            label3.pack(pady=12, padx=10)
            label3.place(relx=0.2, rely=0.4, anchor='e')
            label4 = customtkinter.CTkLabel(master=frame, text="Numar de telefon donator:")
            label4.pack(pady=12, padx=10)
            label4.place(relx=0.2, rely=0.46, anchor='e')
            label5 = customtkinter.CTkLabel(master=frame, text="Nume centru de donare:")
            label5.pack(pady=12, padx=10)
            label5.place(relx=0.2, rely=0.52, anchor='e')
            label6 = customtkinter.CTkLabel(master=frame, text="Data:")
            label6.pack(pady=12, padx=10)
            label6.place(relx=0.2, rely=0.58, anchor='e')
            label7 = customtkinter.CTkLabel(master=frame, text="Ora:")
            label7.pack(pady=12, padx=10)
            label7.place(relx=0.2, rely=0.64, anchor='e')
            entry1 = customtkinter.CTkLabel(master=frame, text=u.nume + " " + u.prenume)
            entry1.pack(pady=12, padx=10)
            entry1.place(relx=0.21, rely=0.28, anchor='w')
            entry2 = customtkinter.CTkLabel(master=frame, text=u.telefon)
            entry2.pack(pady=12, padx=10)
            entry2.place(relx=0.21, rely=0.34, anchor='w')
            entry3a = customtkinter.CTkEntry(master=frame, width=150, placeholder_text="Nume donator")
            entry3a.pack(pady=12, padx=10)
            entry3a.place(relx=0.21, rely=0.4, anchor='w')
            entry3b = customtkinter.CTkEntry(master=frame, width=150, placeholder_text="Prenume donator")
            entry3b.pack(pady=12, padx=10)
            entry3b.place(relx=0.38, rely=0.4, anchor='w')
            entry4 = customtkinter.CTkEntry(master=frame, width=300, placeholder_text="Numar de telefon donator")
            entry4.pack(pady=12, padx=10)
            entry4.place(relx=0.21, rely=0.46, anchor='w')
            entry5 = customtkinter.CTkEntry(master=frame, width=300, placeholder_text="Nume centru de donare")
            entry5.pack(pady=12, padx=10)
            entry5.place(relx=0.21, rely=0.52, anchor='w')
            entry6 = customtkinter.CTkEntry(master=frame, width=300, placeholder_text="Data")
            entry6.pack(pady=12, padx=10)
            entry6.place(relx=0.21, rely=0.58, anchor='w')
            entry7 = customtkinter.CTkEntry(master=frame, width=300, placeholder_text="Ora")
            entry7.pack(pady=12, padx=10)
            entry7.place(relx=0.21, rely=0.64, anchor='w')


            button_programare = customtkinter.CTkButton(master=frame, width=200, text_color=("white"), font=("Roboto", 24),
                                                  height=50, text="Inscriere programare",
                                                  fg_color="#3BB143", hover_color="#0B6623",
                                                  command=lambda: self.inscriere_programare0(frame, root, u, app,
                                                                                     entry3a.get(), entry3b.get(),
                                                                                     entry4.get(), entry5.get(),
                                                                                     entry6.get(), entry7.get()))
            button_programare.pack(pady=12, padx=10)
            button_programare.place(relx=0.5, rely=0.86, anchor='center')

            back_img = customtkinter.CTkImage(Image.open("assets/backarrow.png"), size=(30, 30))
            back_button = customtkinter.CTkButton(master=frame, width=66, height=26, text="", image=back_img,
                                                  fg_color="#00A86B", hover_color="#3F704D",
                                                  command=lambda: self.back_select(frame, root, u, app))
            back_button.pack()
            back_button.place(relx=0.07, rely=0.12, anchor='w')



    def inscriere_programare0(self, frame, root, u, app, e3a, e3b, e4, e5, e6, e7):
        if (app == 0):
            self.connection = mysql.connector.connect(host="localhost", user="root", passwd="a2mEfc@#uo%*cQ",
                                                      database="reteadonaresange")
            self.cursor = self.connection.cursor()

            if(e3a == "-" and e3b == "-" and e4 == "-"):
                self.cursor.execute("""
                                    SELECT COUNT(nume) FROM centredonare
                                    WHERE nume = '{}'
                                    """.format(e5))
                if (self.cursor.fetchall()[0][0] != 0):
                    self.cursor.execute("""
                                        SELECT * FROM centredonare
                                        WHERE nume = '{}'
                                        """.format(e5))
                    results = self.cursor.fetchone()
                    c = Centru()
                    c.load_centru(results[0])
                    self.cursor.execute("""
                                        SELECT COUNT(id_programare) FROM programari
                                        WHERE data = '{}' and ora = {}
                                        """.format(e6, e7))

                    if (self.cursor.fetchall()[0][0] == 0):
                        if (int(e7) <= 24):
                            c.stocsange = c.stocsange + 1
                            c.update_centru()
                            p = Programari()
                            p.id_donator = int(u.id_cont)
                            p.id_beneficiar = 0
                            p.id_centru = int(c.id_centru)
                            p.data = e6
                            p.ora = int(e7)
                            p.insert_programare()
                            eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                            text="Programare facuta cu succes",
                                                            text_color=("Green"), font=("Roboto", 18))
                            eroare.pack(pady=12, padx=10)
                            eroare.place(relx=0.5, rely=0.75, anchor='center')
                        else:
                            eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                            text="Alegeti o ora intre 0 si 24",
                                                            text_color=("Red"), font=("Roboto", 18))
                            eroare.pack(pady=12, padx=10)
                            eroare.place(relx=0.5, rely=0.75, anchor='center')

                    else:
                        eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                        text="Mai exista alta programare deja la aceasta ora",
                                                        text_color=("Red"), font=("Roboto", 18))
                        eroare.pack(pady=12, padx=10)
                        eroare.place(relx=0.5, rely=0.75, anchor='center')

                else:
                    eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                    text="Centrul nu a fost gasit in baza de date",
                                                    text_color=("Red"), font=("Roboto", 18))
                    eroare.pack(pady=12, padx=10)
                    eroare.place(relx=0.5, rely=0.75, anchor='center')

            else:
                self.cursor.execute("""
                        SELECT COUNT(nume) FROM users
                        WHERE nume = '{}' and prenume = '{}' and telefon = '{}'
                        """.format(e3a, e3b, e4))

                if (self.cursor.fetchall()[0][0] != 0):
                    self.cursor.execute("""
                                    SELECT * FROM users
                                    WHERE nume = '{}' and prenume = '{}' and telefon = '{}'
                                    """.format(e3a, e3b, e4))
                    results = self.cursor.fetchone()
                    u2 = User()
                    u2.load_user(results[1])
                    self.cursor.execute("""
                                            SELECT COUNT(id_centru) FROM centredonare
                                            WHERE nume = '{}'
                                            """.format(e5))
                    if (self.cursor.fetchall()[0][0] != 0):
                        self.cursor.execute("""
                                            SELECT * FROM centredonare
                                            WHERE nume = '{}'
                                            """.format(e5))
                        results = self.cursor.fetchone()
                        c = Centru()
                        c.load_centru(results[0])

                        self.cursor.execute("""
                                            SELECT COUNT(id_programare) FROM programari
                                            WHERE data = '{}' and ora = {}
                                            """.format(e6,e7))

                        if (self.cursor.fetchall()[0][0] == 0):
                            if(int(e7) <= 24):
                                p = Programari()
                                p.id_donator = int(u.id_cont)
                                p.id_beneficiar = int(u2.id_cont)
                                p.id_centru = int(c.id_centru)
                                p.data = e6
                                p.ora = int(e7)
                                p.insert_programare()
                                eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                                text="Programare facuta cu succes",
                                                                text_color=("Green"), font=("Roboto", 18))
                                eroare.pack(pady=12, padx=10)
                                eroare.place(relx=0.5, rely=0.75, anchor='center')
                            else:
                                eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                                text="Alegeti o ora intre 0 si 24",
                                                                text_color=("Red"), font=("Roboto", 18))
                                eroare.pack(pady=12, padx=10)
                                eroare.place(relx=0.5, rely=0.75, anchor='center')

                        else:
                            eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                            text="Mai exista alta programare deja la aceasta ora",
                                                            text_color=("Red"), font=("Roboto", 18))
                            eroare.pack(pady=12, padx=10)
                            eroare.place(relx=0.5, rely=0.75, anchor='center')

                    else:
                        eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                        text="Centrul nu a fost gasit in baza de date",
                                                        text_color=("Red"), font=("Roboto", 18))
                        eroare.pack(pady=12, padx=10)
                        eroare.place(relx=0.5, rely=0.75, anchor='center')
                else:
                    eroare = customtkinter.CTkLabel(master=frame, width=600, height=40, text="Beneficiarul nu a fost gasit in baza de date",
                                                    text_color=("Red"), font=("Roboto", 18))
                    eroare.pack(pady=12, padx=10)
                    eroare.place(relx=0.5, rely=0.75, anchor='center')

                self.cursor.execute("""
                                    SELECT COUNT(nume) FROM centredonare
                                    WHERE nume = '{}'
                                    """.format(e5))
            self.connection.close()

        elif(app == 1):
            self.connection = mysql.connector.connect(host="localhost", user="root", passwd="a2mEfc@#uo%*cQ",
                                                      database="reteadonaresange")
            self.cursor = self.connection.cursor()

            if(e3a == "-" and e3b == "-" and e4 == "-"):
                self.cursor.execute("""
                                    SELECT COUNT(nume) FROM centredonare
                                    WHERE nume = '{}'
                                    """.format(e5))
                if (self.cursor.fetchall()[0][0] != 0):
                    self.cursor.execute("""
                                        SELECT * FROM centredonare
                                        WHERE nume = '{}'
                                        """.format(e5))
                    results = self.cursor.fetchone()
                    c = Centru()
                    c.load_centru(results[0])
                    self.cursor.execute("""
                                        SELECT COUNT(id_programare) FROM programari
                                        WHERE data = '{}' and ora = {}
                                        """.format(e6, e7))

                    if (self.cursor.fetchall()[0][0] == 0):
                        if (int(e7) <= 24):
                            if(c.stocsange >= 1):
                                c.stocsange = c.stocsange - 1
                                c.update_centru()
                                p = Programari()
                                p.id_donator = 0
                                p.id_beneficiar = int(u.id_cont)
                                p.id_centru = int(c.id_centru)
                                p.data = e6
                                p.ora = int(e7)
                                p.insert_programare()
                                eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                                text="Programare facuta cu succes",
                                                                text_color=("Green"), font=("Roboto", 18))
                                eroare.pack(pady=12, padx=10)
                                eroare.place(relx=0.5, rely=0.75, anchor='center')
                            else:
                                eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                                text="Centrul ales nu are stocuri de sange disponibile",
                                                                text_color=("Red"), font=("Roboto", 18))
                                eroare.pack(pady=12, padx=10)
                                eroare.place(relx=0.5, rely=0.75, anchor='center')
                        else:
                            eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                            text="Alegeti o ora intre 0 si 24",
                                                            text_color=("Red"), font=("Roboto", 18))
                            eroare.pack(pady=12, padx=10)
                            eroare.place(relx=0.5, rely=0.75, anchor='center')

                    else:
                        eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                        text="Mai exista alta programare deja la aceasta ora",
                                                        text_color=("Red"), font=("Roboto", 18))
                        eroare.pack(pady=12, padx=10)
                        eroare.place(relx=0.5, rely=0.75, anchor='center')

                else:
                    eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                    text="Centrul nu a fost gasit in baza de date",
                                                    text_color=("Red"), font=("Roboto", 18))
                    eroare.pack(pady=12, padx=10)
                    eroare.place(relx=0.5, rely=0.75, anchor='center')

            else:
                self.cursor.execute("""
                        SELECT COUNT(nume) FROM users
                        WHERE nume = '{}' and prenume = '{}' and telefon = '{}'
                        """.format(e3a, e3b, e4))

                if (self.cursor.fetchall()[0][0] != 0):
                    self.cursor.execute("""
                                    SELECT * FROM users
                                    WHERE nume = '{}' and prenume = '{}' and telefon = '{}'
                                    """.format(e3a, e3b, e4))
                    results = self.cursor.fetchone()
                    u2 = User()
                    u2.load_user(results[1])
                    self.cursor.execute("""
                                            SELECT COUNT(id_centru) FROM centredonare
                                            WHERE nume = '{}'
                                            """.format(e5))
                    if (self.cursor.fetchall()[0][0] != 0):
                        self.cursor.execute("""
                                            SELECT * FROM centredonare
                                            WHERE nume = '{}'
                                            """.format(e5))
                        results = self.cursor.fetchone()
                        c = Centru()
                        c.load_centru(results[0])

                        self.cursor.execute("""
                                            SELECT COUNT(id_programare) FROM programari
                                            WHERE data = '{}' and ora = {}
                                            """.format(e6,e7))

                        if (self.cursor.fetchall()[0][0] == 0):
                            if(int(e7) <= 24):
                                p = Programari()
                                p.id_donator = int(u2.id_cont)
                                p.id_beneficiar = int(u.id_cont)
                                p.id_centru = int(c.id_centru)
                                p.data = e6
                                p.ora = int(e7)
                                p.insert_programare()
                                eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                                text="Programare facuta cu succes",
                                                                text_color=("Green"), font=("Roboto", 18))
                                eroare.pack(pady=12, padx=10)
                                eroare.place(relx=0.5, rely=0.75, anchor='center')
                            else:
                                eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                                text="Alegeti o ora intre 0 si 24",
                                                                text_color=("Red"), font=("Roboto", 18))
                                eroare.pack(pady=12, padx=10)
                                eroare.place(relx=0.5, rely=0.75, anchor='center')

                        else:
                            eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                            text="Mai exista alta programare deja la aceasta ora",
                                                            text_color=("Red"), font=("Roboto", 18))
                            eroare.pack(pady=12, padx=10)
                            eroare.place(relx=0.5, rely=0.75, anchor='center')

                    else:
                        eroare = customtkinter.CTkLabel(master=frame, width=600, height=40,
                                                        text="Centrul nu a fost gasit in baza de date",
                                                        text_color=("Red"), font=("Roboto", 18))
                        eroare.pack(pady=12, padx=10)
                        eroare.place(relx=0.5, rely=0.75, anchor='center')
                else:
                    eroare = customtkinter.CTkLabel(master=frame, width=600, height=40, text="Donatorul nu a fost gasit in baza de date",
                                                    text_color=("Red"), font=("Roboto", 18))
                    eroare.pack(pady=12, padx=10)
                    eroare.place(relx=0.5, rely=0.75, anchor='center')

                self.cursor.execute("""
                                    SELECT COUNT(nume) FROM centredonare
                                    WHERE nume = '{}'
                                    """.format(e5))
        self.connection.close()

    def edit_profil(self, frame, root, u, app):
        frame.destroy()
        customtkinter.set_default_color_theme("green")
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Profil utilizator", font=("Roboto", 24))
        label.pack(pady=32, padx=10)

        label1 = customtkinter.CTkLabel(master=frame, text="Username:")
        label1.pack(pady=12, padx=10)
        label1.place(relx=0.12, rely=0.28, anchor='e')
        label2 = customtkinter.CTkLabel(master=frame, text="Parola:")
        label2.pack(pady=12, padx=10)
        label2.place(relx=0.12, rely=0.34, anchor='e')
        label3 = customtkinter.CTkLabel(master=frame, text="Grupa de sange:")
        label3.pack(pady=12, padx=10)
        label3.place(relx=0.12, rely=0.4, anchor='e')
        label4 = customtkinter.CTkLabel(master=frame, text="Nume:")
        label4.pack(pady=12, padx=10)
        label4.place(relx=0.12, rely=0.46, anchor='e')
        label5 = customtkinter.CTkLabel(master=frame, text="Prenume:")
        label5.pack(pady=12, padx=10)
        label5.place(relx=0.12, rely=0.52, anchor='e')
        label6 = customtkinter.CTkLabel(master=frame, text="Email:")
        label6.pack(pady=12, padx=10)
        label6.place(relx=0.12, rely=0.58, anchor='e')
        label7 = customtkinter.CTkLabel(master=frame, text="Telefon:")
        label7.pack(pady=12, padx=10)
        label7.place(relx=0.12, rely=0.64, anchor='e')
        label8 = customtkinter.CTkLabel(master=frame, text="Oras:")
        label8.pack(pady=12, padx=10)
        label8.place(relx=0.12, rely=0.7, anchor='e')
        label9 = customtkinter.CTkLabel(master=frame, text="Adresa:")
        label9.pack(pady=12, padx=10)
        label9.place(relx=0.12, rely=0.76, anchor='e')
        entry1 = customtkinter.CTkLabel(master=frame, text=u.username)
        entry1.pack(pady=12, padx=10)
        entry1.place(relx=0.13, rely=0.28, anchor='w')
        entry2 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Parola", show="*")
        entry2.pack(pady=12, padx=10)
        entry2.place(relx=0.13, rely=0.34, anchor='w')
        entry2.insert(0, u.parola)
        entry3 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Grupa de sange")
        entry3.pack(pady=12, padx=10)
        entry3.place(relx=0.13, rely=0.4, anchor='w')
        entry3.insert(0, u.grupasange)
        entry4 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Nume")
        entry4.pack(pady=12, padx=10)
        entry4.place(relx=0.13, rely=0.46, anchor='w')
        entry4.insert(0, u.nume)
        entry5 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Prenume")
        entry5.pack(pady=12, padx=10)
        entry5.place(relx=0.13, rely=0.52, anchor='w')
        entry5.insert(0, u.prenume)
        entry6 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Email")
        entry6.pack(pady=12, padx=10)
        entry6.place(relx=0.13, rely=0.58, anchor='w')
        entry6.insert(0, u.email)
        entry7 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Telefon")
        entry7.pack(pady=12, padx=10)
        entry7.place(relx=0.13, rely=0.64, anchor='w')
        entry7.insert(0, u.telefon)
        entry8 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Oras")
        entry8.pack(pady=12, padx=10)
        entry8.place(relx=0.13, rely=0.7, anchor='w')
        entry8.insert(0, u.oras)
        entry9 = customtkinter.CTkEntry(master=frame, width = 300, placeholder_text="Adresa")
        entry9.pack(pady=12, padx=10)
        entry9.place(relx=0.13, rely=0.76, anchor='w')
        entry9.insert(0, u.adresa)

        button_edit = customtkinter.CTkButton(master=frame, width=200, text_color=("white"), font=("Roboto", 24),
                                                  height=50, text="Editare profil",
                                                  command=lambda: self.upload_profil(frame, root, u,
                                                                                       entry2.get(), entry3.get(),
                                                                                       entry4.get(), entry5.get(),
                                                                                       entry6.get(), entry7.get(),
                                                                                       entry8.get(), entry9.get()))
        button_edit.pack(pady=12, padx=10)
        button_edit.place(relx=0.5, rely=0.86, anchor='center')

        back_img = customtkinter.CTkImage(Image.open("assets/backarrow.png"), size=(30, 30))
        back_button = customtkinter.CTkButton(master=frame, width=66, height=26, text="", image=back_img,
                                              fg_color="#AEF359", hover_color="#B0FC38",
                                              command=lambda: self.back_select(frame, root, u, app))
        back_button.pack()
        back_button.place(relx=0.07, rely=0.12, anchor='w')

    def upload_profil(self, frame, root, u, e2, e3, e4, e5, e6, e7, e8, e9):
        u.parola = e2
        u.grupasange = e3
        u.nume = e4
        u.prenume = e5
        u.email = e6
        u.telefon = e7
        u.oras = e8
        u.adresa = e9
        u.update_user()
        upload = customtkinter.CTkLabel(master=frame, width=300, height=30,
                                        text="Profil modificat cu succes",
                                        text_color=("Green"), font=("Roboto", 26))
        upload.pack(pady=12, padx=10)
        upload.place(relx=0.7, rely=0.75, anchor='center')


    def back_select(self, frame, root, u, app):
        if(app == 0):
            self.appdonator(frame,root,u)
        elif(app == 1):
            self.appbeneficiar(frame,root,u)

class User:

    def __init__(self, id_cont=0, username="", parola="", grupasange="",nume="", prenume="", email="", telefon="", oras="", adresa=""):
        self.id_cont = id_cont
        self.username = username
        self.parola = parola
        self.grupasange = grupasange
        self.nume = nume
        self.prenume = prenume
        self.email = email
        self.telefon = telefon
        self.oras = oras
        self.adresa = adresa



    def load_user(self, username="", id=-1):
        self.connection = mysql.connector.connect(host="localhost",user="root",passwd="a2mEfc@#uo%*cQ",database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        SELECT * FROM users
        WHERE username = '{}' or id_cont = {}
        """.format(username, id))

        results = self.cursor.fetchone()

        self.id_cont = results[0]
        self.username = results[1]
        self.parola = results[2]
        self.grupasange = results[3]
        self.nume = results[4]
        self.prenume = results[5]
        self.email = results[6]
        self.telefon = results[7]
        self.oras = results[8]
        self.adresa = results[9]

        self.connection.close()

    def insert_user(self):
        self.connection = mysql.connector.connect(host="localhost",user="root",passwd="a2mEfc@#uo%*cQ",database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        INSERT INTO users(username,parola,grupasange,nume,prenume,email,telefon,oras,adresa) 
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(self.username, self.parola,self.grupasange,self.nume,self.prenume,self.email,self.telefon,self.oras,self.adresa))

        self.connection.commit()
        self.connection.close()

    def update_user(self):
        self.connection = mysql.connector.connect(host="localhost",user="root",passwd="a2mEfc@#uo%*cQ",database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        UPDATE users SET parola = '{}',grupasange = '{}',nume = '{}',prenume = '{}',email = '{}',telefon = '{}',oras = '{}',adresa = '{}' WHERE id_cont = {}
        """.format(self.parola,self.grupasange,self.nume,self.prenume,self.email,self.telefon,self.oras,self.adresa,self.id_cont))

        self.connection.commit()
        self.connection.close()


class Programari:

    def __init__(self, id_programare=0, id_donator=0, id_beneficiar=0, id_centru=0, data="", ora=0):
        self.id_programare = id_programare
        self.id_donator = id_donator
        self.id_beneficiar = id_beneficiar
        self.id_centru = id_centru
        self.data = data
        self.ora = ora



    def load_programare(self, id_programare):
        self.connection = mysql.connector.connect(host="localhost",user="root",passwd="a2mEfc@#uo%*cQ",database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        SELECT * FROM programari
        WHERE id_programare = {}
        """.format(id_programare))

        results = self.cursor.fetchone()

        self.id_programare = id_programare
        self.id_donator = results[1]
        self.id_beneficiar = results[2]
        self.id_centru = results[3]
        self.data = results[4]
        self.ora = results[5]

        self.connection.close()

    def insert_programare(self):
        self.connection = mysql.connector.connect(host="localhost",user="root",passwd="a2mEfc@#uo%*cQ",database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        INSERT INTO programari(id_donator,id_beneficiar,id_centru,data,ora) VALUES({},{},{},'{}',{})
        """.format(self.id_donator, self.id_beneficiar,self.id_centru,self.data,self.ora))

        self.connection.commit()
        self.connection.close()

    def update_programare(self):
        self.connection = mysql.connector.connect(host="localhost",user="root",passwd="a2mEfc@#uo%*cQ",database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        UPDATE programari SET id_donator = {},id_beneficiar = {},id_centru = {},data = '{}',ora = {} WHERE id_programare = {}
        """.format(self.id_donator,self.id_beneficiar,self.id_centru,self.data,self.ora,self.id_programare))

        self.connection.commit()
        self.connection.close()


class Istoricdonari:

    def __init__(self, id_donare=0, id_donator=0, id_beneficiar=0, id_centru=0, data="", ora=0, feedbackbeneficiar=""):
        self.id_donare = id_donare
        self.id_donator = id_donator
        self.id_beneficiar = id_beneficiar
        self.id_centru = id_centru
        self.data = data
        self.ora = ora
        self.feedbackbeneficiar = feedbackbeneficiar



    def load_istoricdonare(self, id_donare):
        self.connection = mysql.connector.connect(host="localhost",user="root",passwd="a2mEfc@#uo%*cQ",database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        SELECT * FROM istoricdonari
        WHERE id_donare = {}
        """.format(id_donare))

        results = self.cursor.fetchone()

        self.id_donare = id_donare
        self.id_donator = results[1]
        self.id_beneficiar = results[2]
        self.id_centru = results[3]
        self.data = results[4]
        self.ora = results[5]
        self.feedbackbeneficiar = results[6]

        self.connection.close()

    def insert_istoricdonare(self):
        self.connection = mysql.connector.connect(host="localhost",user="root",passwd="a2mEfc@#uo%*cQ",database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        INSERT INTO istoricdonari(id_donator,id_beneficiar,id_centru,data,ora,feedbackbeneficiar) VALUES
        ({},{},{},'{}',{},'{}')
        """.format(self.id_donator, self.id_beneficiar,self.id_centru,self.data,self.ora,self.feedbackbeneficiar))


        self.connection.commit()
        self.connection.close()

    def update_istoricdonare(self):
        self.connection = mysql.connector.connect(host="localhost",user="root",passwd="a2mEfc@#uo%*cQ",database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        UPDATE istoricdonari SET id_donator = {},id_beneficiar = {},id_centru = {},data = '{}',ora = {},feedback = '{}' WHERE id_donare = {}
        """.format(self.id_donator,self.id_beneficiar,self.id_centru,self.data,self.ora,self.feedbackbeneficiar,self.id_donare))

        self.connection.commit()
        self.connection.close()



class Centru:

    def __init__(self, id_centru=0, nume="", oras="", adresa="",telefon="", stocsange=0):
        self.id_centru = id_centru
        self.nume = nume
        self.oras = oras
        self.adresa = adresa
        self.telefon = telefon
        self.stocsange = stocsange



    def load_centru(self, id_centru):
        self.connection = mysql.connector.connect(host="localhost",user="root",passwd="a2mEfc@#uo%*cQ",database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        SELECT * FROM centredonare
        WHERE id_centru = {}
        """.format(id_centru))

        results = self.cursor.fetchone()

        self.id_centru = id_centru
        self.nume = results[1]
        self.oras = results[2]
        self.adresa = results[3]
        self.telefon = results[4]
        self.stocsange = results[5]


        self.connection.close()

    def insert_centru(self):
        self.connection = mysql.connector.connect(host="localhost",user="root",passwd="a2mEfc@#uo%*cQ",database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        INSERT INTO centredonare VALUES(nume,oras,adresa,telefon,stocsange)
        ('{}','{}','{}','{}',{})
        """.format(self.nume, self.oras,self.adresa,self.telefon,self.stocsange))

        self.connection.commit()
        self.connection.close()

    def update_centru(self):
        self.connection = mysql.connector.connect(host="localhost",user="root",passwd="a2mEfc@#uo%*cQ",database="reteadonaresange")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        UPDATE centredonare SET nume = '{}',oras = '{}',adresa = '{}',telefon = '{}',stocsange = {} WHERE id_centru = {}
        """.format(self.nume,self.oras,self.adresa,self.telefon,self.stocsange,self.id_centru))

        self.connection.commit()
        self.connection.close()




MAIN = Aplicatie()
MAIN.start()
