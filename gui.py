from PIL import Image


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

        self.img = cTK.CTkImage(Image.open("./img/informationButton.png"), size=(30, 30))
        self.img2 = cTK.CTkImage(Image.open("./img/informationButton2.png"), size=(30, 30))

        self.qMark1 = cTK.CTkLabel(master=self, image=self.img, text="")
        self.qMark1.grid(row=1, column=2, columnspan=1)

        def _press(evt=None):
            self.pressed = self.qMark1
            self.qMark1.configure(image=self.img2)

        self.qMark1.bind("<ButtonPress-1>", _press)

        def _leave(evt=None):
            if self.pressed is self.qMark1:
                self.qMark1.configure(image=self.img)
                self.pressed = None

        self.qMark1.bind('<Leave>', _leave)

        def _release(evt=None):
            # Should only do this if we didn't move the mouse away
            if self.pressed is self.qMark1:
                _leave(evt)

        self.qMark1.bind("<ButtonRelease-1>", _release)

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

        self.generateButton = cTK.CTkButton(master=self, text="Generate Config Document")
        self.generateButton.grid(row=6, column=0, columnspan=3, padx=20, pady=(20, 20))

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
