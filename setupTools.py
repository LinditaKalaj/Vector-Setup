import sys
from pathlib import Path

import anki_vector
import requests


class setupTools:
    def __init__(self, name, ip, serial, email, password):
        self.name = name
        self.ip = ip
        self.serial = serial
        self.email = email
        self.password = password

    def run(self):
        home = Path.home()
