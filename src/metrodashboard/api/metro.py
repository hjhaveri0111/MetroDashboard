import requests
import json
import os

class MetroClient:
    __WMATA_URL = "https://api.wmata.com"

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
