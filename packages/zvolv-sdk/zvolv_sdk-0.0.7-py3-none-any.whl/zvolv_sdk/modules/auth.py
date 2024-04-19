import requests
import hashlib

class Auth:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def login(self, email, password):
        """Authenticate a user and store their auth token."""
        url = f"{self.base_url}/rest/v17/user/login"
        sha512pwd = hashlib.sha512(password.encode('utf-8')).hexdigest()
        data = {'email': email, 'password': sha512pwd}
        response = self.session.post(url, json=data, headers={'Content-Type': 'application/json', 'jwt': True,
        'businessDomain': 'kapilwf', 'businessTagId' : '449VZ2DY54AF3'})
        if response.status_code == 200:
            resp = response.json()
            if resp.get('error') == False:
                token = resp['loginToken']
                self.session.headers.update({'Authorization': f"Bearer {token}"})
                print(self.session.headers)
            else:
                print("Login Failed")
                print(response.json())

        return response.json()