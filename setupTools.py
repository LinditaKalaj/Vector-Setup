import configparser
import json
import os
from pathlib import Path
import socket
import grpc
import requests
from anki_vector import messaging
from api import Api
from cryptography import x509
from cryptography.hazmat.backends import default_backend


class SetupTools:
    # Gets params from the gui needed for the certificate
    def __init__(self, name, ip, serial, email, password, app_gui):
        self.name = name
        self.ip = ip
        self.serial = serial
        self.login_credentials = {'username': email, 'password': password}
        self.api = Api()
        self.app_gui = app_gui
        self.run()

    def run(self):
        # Resets the progress bar
        self.app_gui.progressBar.set(0)

        # Gets session information from users login and password, exits run method if no match
        session_id = self.get_session_id()
        if not session_id or not session_id.get("session"):
            return

        # Gets certificate via api request using Vector's serial, exits if no cert is provided
        cert = self.get_cert()
        if not cert:
            return

        # Writes the certificate to the users home directory
        cert_file = self.save_cert(cert)

        # Validates if Vectors name matches the one on the certificate, exits method if cert is not valid
        validate_cert = self.validate_cert_name(cert_file)
        if not validate_cert:
            return

        # Getting GUID with ip, credentials from the cert and name, exits method if there was an error
        guid = self.user_authentication(session_id["session"]["session_token"], cert, self.ip, self.name)
        if guid == "error":
            return
        self.write_config(cert_file, guid)

        # Takes progress bar to the last step
        self.app_gui.progressInfo.configure(text="Done!", text_color="white")
        self.app_gui.progressBar.step()

    def get_session_id(self):
        # Moves progress bar and notifies user
        self.app_gui.progressInfo.configure(text="Verifying Login Info...", text_color="white")
        self.app_gui.progressBar.step()

        # create a POST request to grab session information
        r = requests.post(self.api.urls, data=self.login_credentials, headers=self.api.headers)
        session_id = json.loads(r.content)

        # Alerts user if request was unsuccessful, else return the session information
        if r.status_code != 200:
            self.app_gui.show_error_dialog(session_id.get('message'))
            self.app_gui.progressInfo.configure(text="Could not verify login info!", text_color="red")
            self.app_gui.emailEntry.configure(border_color="#9c2b2e")
            self.app_gui.passWordEntry.focus_force()
            self.app_gui.passWordEntry.configure(border_color="#9c2b2e")
            return None
        else:
            return json.loads(r.content)

    def get_cert(self):
        # Moves progress bar and notifies user
        self.app_gui.progressInfo.configure(text="Getting your certificate...", text_color="white")
        self.app_gui.progressBar.step()

        # Get request made to anki to fetch cert based on serial provided by user
        r = requests.get('https://session-certs.token.global.anki-services.com/vic/{}'.format(self.serial))

        # Alerts user if request was unsuccessful, else return cert
        if r.status_code != 200:
            self.app_gui.show_error_dialog("Something went wrong! You entered ({}). Please make sure the serial "
                                           "number is correct, and try again.".format(self.serial))
            print("error")
            self.app_gui.progressInfo.configure(text="Could not verify Vectors serial number!", text_color="red")
            self.app_gui.snEntry.focus_force()
            self.app_gui.snEntry.configure(border_color="#9c2b2e")
            return None

        return r.content

    def save_cert(self, cert):
        # Paths to cert file location, located in user/.anki_vector location
        home_dir = Path.home()
        cert_dir = home_dir / ".anki_vector"
        os.makedirs(str(cert_dir), exist_ok=True)
        cert_file = str(cert_dir / "{name}-{serial}.cert".format(name=self.name, serial=self.serial))

        # Moves progress bar and notifies user
        self.app_gui.progressInfo.configure(text="Writing certificate file to '{}'...\n".format(cert_file), text_color="white")
        self.app_gui.progressBar.step()

        # Write cert to file
        with os.fdopen(os.open(cert_file, os.O_WRONLY | os.O_CREAT, 0o600), 'wb') as f:
            f.write(cert)
        return cert_file

    def validate_cert_name(self, cert):
        # Moves progress bar and notifies user
        self.app_gui.progressInfo.configure(text="Validating certificate...", text_color="white")
        self.app_gui.progressBar.step()

        # Opens cert file and compares the user given Vectors name to the name in the cert
        with open(cert, "rb") as f:
            cert_file = f.read()
            cert = x509.load_pem_x509_certificate(cert_file, default_backend())
            for fields in cert.subject:
                current = str(fields.oid)
                if "commonName" in current:
                    common_name = fields.value
                    if common_name != self.name:
                        self.app_gui.show_error_dialog("The name of the certificate ({}) does not match the name "
                                                       "provided ({}). Please verify the name/serial, and try again."
                                                       .format(common_name, self.name))
                        self.app_gui.progressInfo.configure(text="Could not validate the certificate!",
                                                            text_color="red")
                        self.app_gui.nameEntry.focus_force()
                        self.app_gui.nameEntry.configure(border_color="#9c2b2e")
                        return False
                    else:
                        return True

    def user_authentication(self, session_id: bytes, cert: bytes, ip: str, name: str) -> str:
        # Moves progress bar and notifies user
        self.app_gui.progressInfo.configure(text="Authenticating...", text_color="white")
        self.app_gui.progressBar.step()

        # Pin the robot certificate for opening the channel
        creds = grpc.ssl_channel_credentials(root_certificates=cert)
        channel = grpc.secure_channel("{}:443".format(ip), creds,
                                      options=(("grpc.ssl_target_name_override", name,),))

        # Verify the connection to Vector is able to be established (client-side)
        try:
            # Explicitly grab _channel._channel to test the underlying grpc channel directly
            grpc.channel_ready_future(channel).result(timeout=15)
        except grpc.FutureTimeoutError:
            self.app_gui.show_error_dialog("\nUnable to connect to Vector\nPlease be sure to connect via the Vector "
                                           "companion app first, and connect your computer to the same network as "
                                           "your Vector.")
            self.app_gui.progressInfo.configure(text="Could not connect to Vector!",
                                                text_color="red")
            return "error"

        try:
            # Tries to get authorization after connection
            interface = messaging.client.ExternalInterfaceStub(channel)
            request = messaging.protocol.UserAuthenticationRequest(
                user_session_id=session_id.encode('utf-8'),
                client_name=socket.gethostname().encode('utf-8'))
            response = interface.UserAuthentication(request)
            if response.code != messaging.protocol.UserAuthenticationResponse.AUTHORIZED:  # pylint: disable=no-member
                self.app_gui.show_error_dialog("\nFailed to authorize request:\nPlease be sure to first set up Vector "
                                               "using the companion app.")
                self.app_gui.progressInfo.configure(text="Could not connect to Vector!",
                                                    text_color="red")
                return "error"
        except grpc.RpcError as e:
            self.app_gui.show_error_dialog("\nFailed to authorize request:\n An unknown error occurred '{}'".format(e))
            self.app_gui.progressInfo.configure(text="Could not connect to Vector!",
                                                text_color="red")
            return "error"

        return response.client_token_guid

    def write_config(self, cert_file=None, guid=None, clear=True):
        # Moves progress bar and notifies user
        self.app_gui.progressInfo.configure(text="Updating certificate with GUID...", text_color="white")
        self.app_gui.progressBar.step()

        # Gets config file location
        home = Path.home()
        config_file = str(home / ".anki_vector" / "sdk_config.ini")
        config = configparser.ConfigParser(strict=False)

        # Writes Vector's information to the config file
        try:
            config.read(config_file)
        except configparser.ParsingError:
            if os.path.exists(config_file):
                os.rename(config_file, config_file + "-error")
        if clear:
            config[self.serial] = {}
        if cert_file:
            config[self.serial]["cert"] = cert_file
        if self.ip:
            config[self.serial]["ip"] = self.ip
        if self.name:
            config[self.serial]["name"] = self.name
        if guid:
            config[self.serial]["guid"] = guid.decode("utf-8")
        temp_file = config_file + "-temp"
        if os.path.exists(config_file):
            os.rename(config_file, temp_file)
        try:
            with os.fdopen(os.open(config_file, os.O_WRONLY | os.O_CREAT, 0o600), 'w') as f:
                config.write(f)
        except Exception as e:
            if os.path.exists(temp_file):
                os.rename(temp_file, config_file)
            raise e
        else:
            if os.path.exists(temp_file):
                os.remove(temp_file)
