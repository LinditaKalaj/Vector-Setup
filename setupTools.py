import json
import os
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

        self.run()

    def run(self):
        session_id = self.get_session_id()
        cert = self.get_cert()
        if not session_id or not session_id.get("session"):
            return
        if not cert:
            return
        cert_file = self.save_cert(cert)
        validate_cert = self.validate_cert_name(cert_file)
        if not validate_cert:
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
        if r.status_code != 200:
            self.app_gui.show_error_dialog("Something went wrong! You entered ({}). Please make sure the serial "
                                           "number is correct, and try again.".format(self.serial))
            print("error")
            return None
        cert = r.content
        print(cert)
        return cert

    def save_cert(self, cert):
        home_dir = Path.home()
        cert_dir = home_dir / ".anki_vector"
        os.makedirs(str(cert_dir), exist_ok=True)
        cert_file = str(cert_dir / "{name}-{serial}.cert".format(name=self.name, serial=self.serial))
        print("Writing certificate file to '{}'...\n".format(cert_file))
        with os.fdopen(os.open(cert_file, os.O_WRONLY | os.O_CREAT, 0o600), 'wb') as f:
            f.write(cert)
        return cert_file

    def validate_cert_name(self, cert):
        with open(cert, "rb") as f:
            cert_file = f.read()
            cert = x509.load_pem_x509_certificate(cert_file, default_backend())
            for fields in cert.subject:
                current = str(fields.oid)
                if "commonName" in current:
                    common_name = fields.value
                    if common_name != self.name:
                        self.app_gui.show_error_dialog("The name of the certificate ({}) does not match the name "
                                                       "provided ({}). Please verify the name, and try again."
                                                       .format(common_name, self.name))
                        return False
                    else:
                        return True

