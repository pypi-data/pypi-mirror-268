import requests
import hashlib

class Workspace:
    workspaceInstance = None
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url
    
    def init(self, domain):
        """Set the domain for the workspace."""
        self.session.headers.update({'domain': domain})
        """Fetch workspace details from domain."""
        url = f"{self.base_url}/rest/v17/organisation/web/config/{domain}"
        response = self.session.get(url)
        if response.status_code == 200:
            resp = response.json()
            if resp.get('error') == False:
                self.workspaceInstance = resp['data']
                print("Init Success")
                print(response.json())
            else:
                print("Init Failed")
                print(response.json())

        return response.json()