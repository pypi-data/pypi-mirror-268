import requests
from modules.auth import Auth

class ZvolvClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.auth = Auth(self.session, self.base_url)