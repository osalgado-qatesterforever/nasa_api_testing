import requests

class APIClient:
    BASE_URL = "https://api.nasa.gov"

    def __init__(self, ext_params=None):
        self.params = {
            'api_key':"hH21kco9yqxWAEDKc2WoY7Pe6OdQw8EjjbjwgHCc"
            }
        if ext_params is not None:
            self.params.update(ext_params)
        
    def get(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, params=self.params)
        return response
    
    def post(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url, params=self.params)
        return response

    def put(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.put(url, params=self.params)
        return response   

    def delete(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.delete(url, params=self.params)
        return response