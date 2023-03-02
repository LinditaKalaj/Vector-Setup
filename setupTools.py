import json
import sys
from pathlib import Path
import requests
from api import Api
from cryptography import x509
from cryptography.hazmat.backends import default_backend


class SetupTools:
    def __init__(self, name, ip, serial, email, password, app_gui):
        self.name = name
        self.ip = ip
        self.serial = serial
        self.login_credentials = {'username': email, 'password': password}
        self.api = Api()
        self.app_gui = app_gui
        self.cert = None

        self.run()

    def run(self):
        home_dir = Path.home()
        cert_dir = home_dir / ".anki_vector"
        session_id = self.get_session_id()
        if not session_id or not session_id.get("session"):
            return

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

    def get_cert(self):
        r = requests.get('https://session-certs.token.global.anki-services.com/vic/{}'.format(self.serial))
        message = json.loads(r.content)
        if r.status_code != 200:
            self.app_gui.show_error_dialog(message.get('message'))
            return None
        cert = r.content
        return cert
