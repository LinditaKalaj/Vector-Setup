import anki_vector


class Api:
    def __init__(self):
        self.headers = {
            'User-Agent': f'Vector-sdk/{anki_vector.__version__}',
            'Anki-App-Key': 'aung2ieCho3aiph7Een3Ei'
        }
        self.urls = 'https://accounts.api.anki.com/1/sessions'
