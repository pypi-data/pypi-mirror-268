import requests

class Auth:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def login(self, email, password):
        """Authenticate a user and store their auth token."""
        url = f"{self.base_url}/rest/v17/user/login"
        data = {'email': email, 'password': password}
        response = self.session.post(url, json=data, headers={'Content-Type': 'application/json', 'jwt': True,
        'businessDomain': 'kapilwf', 'businessTagId' : '449VZ2DY54AF3'})
        if response.status_code == 200:
            print("Login Successful")
            print(response.json())
            self.session.headers.update({'Authorization': f"Bearer {response.json()['token']}"})
        return response.json()