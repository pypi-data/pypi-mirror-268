import requests

from e2e_cli.core.constants import BASE_URL

class ApiClient:
    def __init__(self, api_key, auth_token, project_id=None, location="Delhi"):
        self.api_key = api_key
        self.auth_token = f"Bearer {auth_token}"
        self.project_id = project_id
        self.location = location
    
    def _get_headers(self):
        return {
            'Authorization': self.auth_token,
            'Content-Type': 'application/json',
            'User-Agent' : 'cli-e2e',
        }
    
    def _get_default_query_params(self):
        return {
            "apikey": self.api_key,
            "location": self.location,
        }
    
    def get_response(self, url, method, payload={}, query_params={}):
        api_endpoint = f"{BASE_URL}{url}"
        headers = self._get_headers()
        query_params.update(self._get_default_query_params())
        if self.project_id:
            query_params["project_id"] = self.project_id
        
        try:
            response = requests.request(method=method, url=api_endpoint, headers=headers,
                                        params=query_params, data=payload)
        except Exception as e:
            print(f"There is some exception occured. Kindly try after some time. error-{str(e)}")
            return None
        try: 
            return response.json()
        except Exception as e:
            print("There is some issue in getting response.")