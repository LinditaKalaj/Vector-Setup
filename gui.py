import re
import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.emailPattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        self.ipPattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
        self.namePattern1 = r'[Vv]ector.[A-Za-z0-9]{4}'
        self.namePattern2 = r'Vector-[A-Z0-9]{4}'

        self.generateButton = None
        self.passWordEntry = None
        self.passWordLabel = None
        self.emailEntry = None
        self.emailLabel = None
        self.snEntry = None
        self.snLabel = None
        self.ipEntry = None
        self.ipLabel = None
        self.nameEntry = None
        self.nameLabel = None
        self.header = None
        self.sidebar_frame = None

        self.configure_style()
        self.configure_grid()
        self.configure_frame()
        self.configure_items()
        self.set_bindings()

    def configure_style(self):
        self.configure(background='#303030')
        self.title("ezVector Setup")
        self.geometry("600x800")
        self.minsize(400, 600)
        self.iconbitmap("./img/myIcon.ico")
        ctk.set_default_color_theme("green")

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
        self.nameEntry.bind("<Key>", lambda event: self.nameEntry.configure(fg_color="gray21"))
        self.ipEntry.bind("<Key>", lambda event: self.ipEntry.configure(fg_color="gray21"))
        self.snEntry.bind("<Key>", lambda event: self.snEntry.configure(fg_color="gray21"))
        self.emailEntry.bind("<Key>", lambda event: self.emailEntry.configure(fg_color="gray21"))
        self.passWordEntry.bind("<Key>", lambda event: self.passWordEntry.configure(fg_color="gray21"))

    def send_to_setup_tools(self):
        name = self.validate_name()
        ip = self.validate_ip()
        serial = self.validate_sn()
        email = self.validate_email()
        password = self.validate_password()

    def validate_name(self):
        name = self.nameEntry.get()
        if len(name) == 4:
            name = "Vector-{}".format(name.upper())
        if re.match(self.namePattern1, name):
            name = "V{}-{}".format(name[1:-5], name[-4:].upper())
        if re.match(self.namePattern2, name):
            return name
        else:
            self.nameEntry.focus_force()
            self.nameEntry.configure(fg_color="tomato4")
            return None

    def validate_ip(self):
        ip = self.ipEntry.get()
        if re.match(self.ipPattern, ip):
            return ip
        else:
            self.ipEntry.focus_force()
            self.ipEntry.configure(fg_color="tomato4")
            return None

    def validate_sn(self):
        sn = self.snEntry.get()
        if len(sn) == 8:
            return sn
        else:
            self.snEntry.focus_force()
            self.snEntry.configure(fg_color="tomato4")
            return None

    def validate_email(self):
        email = self.emailEntry.get()
        if re.match(self.emailPattern, email):
            return email
        else:
            self.emailEntry.focus_force()
            self.emailEntry.configure(fg_color="tomato4")
            return None

    def validate_password(self):
        pw = self.passWordEntry.get()
        if len(pw) > 0:
            return pw
        else:
            self.passWordEntry.focus_force()
            self.passWordEntry.configure(fg_color="tomato4")
            return None

    def configure_frame(self):
        self.sidebar_frame = ctk.CTkFrame(self, corner_radius=0, width=600)
        self.sidebar_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(0, weight=1)
        self.sidebar_frame.grid_columnconfigure(0, weight=1)
        self.sidebar_frame.grid_columnconfigure(1, weight=1)
        self.sidebar_frame.grid_columnconfigure(2, weight=1)

    def configure_items(self):
        self.header = ctk.CTkLabel(self.sidebar_frame,
                                   text="Welcome to ezVector setup!\n"
                                        "Fill in this form to generate "
                                        "a certificate for your robot")
        self.header.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        self.nameLabel = ctk.CTkLabel(master=self, text="Vector's Name: ")
        self.nameLabel.grid(row=1, column=0, padx=20, pady=20)

        self.nameEntry = ctk.CTkEntry(master=self, width=200, placeholder_text="ex. C5W2")
        self.nameEntry.grid(row=1, column=1, padx=20, pady=20)

        self.ipLabel = ctk.CTkLabel(master=self, text="Vector's IP: ")
        self.ipLabel.grid(row=2, column=0, padx=20, pady=20)

        self.ipEntry = ctk.CTkEntry(master=self, width=200, placeholder_text="ex. 192.168.30.59")
        self.ipEntry.grid(row=2, column=1, padx=20, pady=20)

        self.snLabel = ctk.CTkLabel(master=self, text="Vector's Serial: ")
        self.snLabel.grid(row=3, column=0, padx=20, pady=20)

        self.snEntry = ctk.CTkEntry(master=self, width=200, placeholder_text="ex. 00e20100")
        self.snEntry.grid(row=3, column=1, padx=20, pady=20)

        self.emailLabel = ctk.CTkLabel(master=self, text="Your Anki Email: ")
        self.emailLabel.grid(row=4, column=0, padx=20, pady=20)

        self.emailEntry = ctk.CTkEntry(master=self, width=200, placeholder_text="ex. garfieldCat@gmail.com")
        self.emailEntry.grid(row=4, column=1, padx=20, pady=20)

        self.passWordLabel = ctk.CTkLabel(master=self, text="Your Anki Password: ")
        self.passWordLabel.grid(row=5, column=0, padx=20, pady=20)

        self.passWordEntry = ctk.CTkEntry(master=self, width=200, placeholder_text="***********", show="*")
        self.passWordEntry.grid(row=5, column=1, padx=20, pady=20)

        self.generateButton = ctk.CTkButton(master=self, text="Generate Config Document",
                                            command=self.send_to_setup_tools)
        self.generateButton.grid(row=6, column=0, columnspan=3, padx=20, pady=(20, 20))
