import json
import sys
import time
from pathlib import Path
import anki_vector
import requests
from api import Api


class SetupTools:
    def __init__(self, name, ip, serial, email, password, app_gui):
        self.name = name
        self.ip = ip
        self.serial = serial
        self.login_credentials = {'username': email, 'password': password}
        self.api = Api()
        self.app_gui = app_gui

        self.run()

    def run(self):
        home_dir = Path.home()
        cert_dir = home_dir / ".anki_vector"
        session_id = self.get_session_id()
        if session_id and session_id.get("session"):
            print("finish this later")

    def get_session_id(self):
        print("obtaining sessionId ")
        print(self.api.urls, self.login_credentials, self.api.headers)
        r = requests.post(self.api.urls, data=self.login_credentials, headers=self.api.headers)
        session_id = json.loads(r.content)
        if r.status_code != 200:
            self.app_gui.show_error_dialog(session_id.get('message'))
            return None
        else:
            print("done")
            return json.loads(r.content)


