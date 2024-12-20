import requests
from requests import Response
from src.utils.tools import get_api_key


class APIClient:
    BASE_URL = "https://api.nasa.gov"

    def __init__(self, ext_params=None):
        api_key = get_api_key()
        self.params = {
            'api_key':api_key
            }
        if ext_params is not None:
            self.params.update(ext_params)
        
    def get(self, endpoint:str) -> Response:
        """ Makes a GET request """
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, params=self.params)
        return response
    
    def post(self, endpoint:str) -> Response:
        """ Makes a POST request """
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url, params=self.params)
        return response

    def put(self, endpoint:str) -> Response:
        """ Makes a PUT request """
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.put(url, params=self.params)
        return response   

    def delete(self, endpoint:str) -> Response:
        """ Makes a DELETE request """
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.delete(url, params=self.params)
        return response