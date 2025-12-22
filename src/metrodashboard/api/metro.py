import requests
import json
import os

class MetroClient:
    __WMATA_URL = "https://api.wmata.com"
    __API_PRIMARY_KEY = os.getenv("API_KEY")

    def make_api_request(self, endpoint: str):
        request_url = f'{self.__WMATA_URL}/{endpoint}'
        parameters = {
            'contentType': 'json'
        }
        headers = {
            'Cache-Control': 'no-cache',
            'api_key': os.getenv("API_KEY")
        }

        response = requests.get(request_url,params=parameters, headers=headers)
        return json.loads(response.text)
