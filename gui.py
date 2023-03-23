import asyncio
import re
import threading
import customtkinter as ctk
from setupTools import SetupTools
from tkinter import messagebox


class Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Get event loop for async call to SetupTools
        self.loop = asyncio.get_event_loop()
        self.setupTool = None

        # Patterns for validation
        self.emailPattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        self.ipPattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
        self.namePattern1 = r'[Vv]ector.[A-Za-z0-9]{4}'
        self.namePattern2 = r'Vector-[A-Z0-9]{4}'
        self.namePattern3 = r'VECTOR.[A-Za-z0-9]{4}'

        # Gui objects instantiated in init, so I can access it later
        self.progressInfo = None
        self.progressBar = None
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
        self.header_frame = None

        # Configure styles and gui objects
        self.configure_style()
        self.configure_grid()
        self.configure_header_frame()
        self.configure_items()
        self.set_bindings()

    def configure_style(self):
        self.configure(background='#303030')
        self.title("ezVector Setup")
        ctk.set_default_color_theme("green")

        # Set min and max sizes
        width = 500
        height = 700
        self.minsize(400, 600)
        self.maxsize(500, 700)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        # Centers window based on users monitor
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def configure_grid(self):
        # Configures row and col weights
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
        # Set on key press functions for all entries
        self.nameEntry.bind("<Key>", lambda event: self.nameEntry.configure(border_color=["#979DA2", "#565B5E"]))
        self.ipEntry.bind("<Key>", lambda event: self.ipEntry.configure(border_color=["#979DA2", "#565B5E"]))
        self.snEntry.bind("<Key>", lambda event: self.snEntry.configure(border_color=["#979DA2", "#565B5E"]))
        self.emailEntry.bind("<Key>", lambda event: self.emailEntry.configure(border_color=["#979DA2", "#565B5E"]))
        self.passWordEntry.bind("<Key>",
                                lambda event: self.passWordEntry.configure(border_color=["#979DA2", "#565B5E"]))

    def validate_all(self):
        # Sends all entry inputs to their own validator method
        name = self.validate_name()
        ip = self.validate_ip()
        serial = self.validate_sn()
        email = self.validate_email()
        password = self.validate_password()

        # If all inputs are valid start a thread to get the cert asynchronously
        if name and ip and serial and email and password:
            self.generateButton.configure(state="disabled", command=None)
            threading.Thread(target=self.async_thread, args=(name, ip, serial, email, password,)).start()

    def validate_name(self):
        name = self.nameEntry.get()

        # Makes sure the input is only XXXX or Vector-XXXX
        if len(name) == 4:
            name = "Vector-{}".format(name.upper())
        if re.match(self.namePattern1, name) or re.match(self.namePattern3, name):
            name = "V{}-{}".format(name[1:-5].lower(), name[-4:].upper())
        if re.match(self.namePattern2, name):
            return name
        else:
            self.nameEntry.focus_force()
            self.nameEntry.configure(border_color="#9c2b2e")
            return None

    def validate_ip(self):
        ip = self.ipEntry.get()
        if re.match(self.ipPattern, ip):
            return ip
        else:
            self.ipEntry.focus_force()
            self.ipEntry.configure(border_color="#9c2b2e")
            return None

    def validate_sn(self):
        sn = self.snEntry.get()
        if len(sn) == 8 and sn.isalnum():
            return sn.lower()
        else:
            self.snEntry.focus_force()
            self.snEntry.configure(border_color="#9c2b2e")
            return None

    def validate_email(self):
        email = self.emailEntry.get()
        if re.match(self.emailPattern, email):
            return email
        else:
            self.emailEntry.focus_force()
            self.emailEntry.configure(border_color="#9c2b2e")
            return None

    def validate_password(self):
        pw = self.passWordEntry.get()
        if len(pw) > 0:
            return pw
        else:
            self.passWordEntry.focus_force()
            self.passWordEntry.configure(border_color="#9c2b2e")
            return None

    def configure_header_frame(self):
        # Sets weight of row and cols for info header
        self.header_frame = ctk.CTkFrame(self, corner_radius=0, width=600)
        self.header_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.header_frame.grid_rowconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=1)
        self.header_frame.grid_columnconfigure(2, weight=1)

    def configure_items(self):
        # Assigns items to ctk objects and set them on the grid
        self.header = ctk.CTkLabel(self.header_frame,
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

        self.generateButton = ctk.CTkButton(master=self, state="normal", text="Generate Config Document",
                                            command=lambda: self.validate_all())
        self.generateButton.grid(row=6, column=0, columnspan=3, padx=20, pady=(20, 20))

        self.progressInfo = ctk.CTkLabel(master=self, text=" ")
        self.progressInfo.grid(row=7, column=0, columnspan=3)

        self.progressBar = ctk.CTkProgressBar(master=self, mode="determinate", determinate_speed=7.123, width=600,
                                              corner_radius=0)

        self.progressBar.grid(row=8, column=0, columnspan=3)
        self.progressBar.set(0)

    # Runs async thread
    def async_thread(self, name, ip, serial, email, password):
        self.loop.run_until_complete(self.send_to_setuptools(name, ip, serial, email, password))

    # Creates an asyncio task and adds a callback function
    async def send_to_setuptools(self, name, ip, serial, email, password):
        task = asyncio.create_task(self.run_setuptools(name, ip, serial, email, password))
        task.add_done_callback(self.callback)
        await task

    # Allows user to press the generate button after task is complete
    def callback(self, task):
        self.generateButton = ctk.CTkButton(master=self, state="normal", text="Generate Config Document",
                                            command=lambda: self.validate_all())
        self.generateButton.grid(row=6, column=0, columnspan=3, padx=20, pady=(20, 20))

    async def run_setuptools(self, name, ip, serial, email, password):
        SetupTools(name, ip, serial, email, password, self)

    def show_error_dialog(self, message):
        messagebox.showerror('Error!', message)
