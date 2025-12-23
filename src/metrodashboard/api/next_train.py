from metrodashboard.api.metro import MetroClient
from metrodashboard.models.rail_prediction import RailPrediction
import json

class NextTrain:
    _BASE_PATH = 'StationPrediction.svc/json/'
    def __init__(self, client: MetroClient):
        self.client = client
        with open('stations.json', 'r') as f:
            self.stations = json.load(f)
    
    def get_next_trains_for_station(self, station_name: str) -> list[RailPrediction]:
        station_code = self.stations[station_name]
        endpoint = f'{self._BASE_PATH}/GetPrediction/{station_code}'

        return [RailPrediction(prediction) for prediction in self.client.make_api_request(endpoint)['Trains']]


        
