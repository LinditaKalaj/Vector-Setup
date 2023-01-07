import re

import customtkinter as cTK


class App(cTK.CTk):
    def __init__(self):
        super().__init__()
        self.iconbitmap("./img/myIcon.ico")
        cTK.set_default_color_theme("green")
        self.configure_style()

        self.configure_grid()

        self.title("ezVector Setup")
        self.geometry("600x800")
        self.minsize(400, 600)

        self.sidebar_frame = cTK.CTkFrame(self, corner_radius=0, width=600)
        self.sidebar_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(0, weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)
        self.sidebar_frame.grid_columnconfigure(1, weight=1)
        self.sidebar_frame.grid_columnconfigure(2, weight=1)

        self.header = cTK.CTkLabel(self.sidebar_frame,
                                   text="Welcome to ezVector setup!\n"
                                        "Fill in this form to generate "
                                        "a certificate for your robot")
        self.header.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        self.nameLabel = cTK.CTkLabel(master=self, text="Vector's Name: ")
        self.nameLabel.grid(row=1, column=0, padx=20, pady=20)

        self.nameEntry = cTK.CTkEntry(master=self, width=200, placeholder_text="ex. C5W2")
        self.nameEntry.grid(row=1, column=1, padx=20, pady=20)

        self.ipLabel = cTK.CTkLabel(master=self, text="Vector's IP: ")
        self.ipLabel.grid(row=2, column=0, padx=20, pady=20)

        self.ipEntry = cTK.CTkEntry(master=self, width=200, placeholder_text="ex. 192.168.30.59")
        self.ipEntry.grid(row=2, column=1, padx=20, pady=20)

        self.snLabel = cTK.CTkLabel(master=self, text="Vector's Serial: ")
        self.snLabel.grid(row=3, column=0, padx=20, pady=20)

        self.snEntry = cTK.CTkEntry(master=self, width=200, placeholder_text="ex. 00e20100")
        self.snEntry.grid(row=3, column=1, padx=20, pady=20)

        self.emailLabel = cTK.CTkLabel(master=self, text="Your Anki Email: ")
        self.emailLabel.grid(row=4, column=0, padx=20, pady=20)

        self.emailEntry = cTK.CTkEntry(master=self, width=200, placeholder_text="ex. garfieldCat@gmail.com")
        self.emailEntry.grid(row=4, column=1, padx=20, pady=20)

        self.passWordLabel = cTK.CTkLabel(master=self, text="Your Anki Password: ")
        self.passWordLabel.grid(row=5, column=0, padx=20, pady=20)

        self.passWordEntry = cTK.CTkEntry(master=self, width=200, placeholder_text="***********", show="*")
        self.passWordEntry.grid(row=5, column=1, padx=20, pady=20)

        self.generateButton = cTK.CTkButton(master=self, text="Generate Config Document", command=self.send_to_setup_tools)
        self.generateButton.grid(row=6, column=0, columnspan=3, padx=20, pady=(20, 20))

        self.set_bindings()

    def configure_style(self):
        self.configure(background='#303030')

    def configure_grid(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def set_bindings(self):
        self.nameEntry.bind("<Key>", lambda event: self.turn_back_fg(self.nameEntry))
        self.ipEntry.bind("<Key>", lambda event: self.turn_back_fg(self.ipEntry))
        self.snEntry.bind("<Key>", lambda event: self.turn_back_fg(self.snEntry))
        self.emailEntry.bind("<Key>", lambda event: self.turn_back_fg(self.emailEntry))

    def send_to_setup_tools(self):
        name = self.validate_name(self.nameEntry)
        ip = self.validate_ip(self.ipEntry)
        serial = self.validate_sn(self.snEntry)
        email = self.validate_email(self.emailEntry)
        password = self.passWordEntry.get()

    def validate_name(self, name_entry):
        name = name_entry.get()
        if len(name) == 4:
            name = "Vector-{}".format(name.upper())
        if re.match("[Vv]ector.[A-Za-z0-9]{4}", name):
            name = "V{}-{}".format(name[1:-5], name[-4:].upper())
        if re.match("Vector-[A-Z0-9]{4}", name):
            return name
        else:
            self.highlight_error(name_entry)

    def validate_ip(self, ip_entry):
        ip = ip_entry.get()
        if re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
            return ip
        else:
            self.highlight_error(ip_entry)

    def validate_sn(self, sn_entry):
        sn = sn_entry.get()
        if len(sn) == 8:
            return sn
        else:
            self.highlight_error(sn_entry)

    def validate_email(self, email_entry):
        email = email_entry.get()
        if re.match("r^\S+@\S+\.\S+$", email):
            return email
        else:
            self.highlight_error(email_entry)

    def highlight_error(self, entry):
        entry.focus_force()
        entry.configure(fg_color="tomato4")

    def turn_back_fg(self, entry):
        entry.configure(fg_color="gray21")
