from metrodashboard.api.metro import MetroClient
from metrodashboard.models.rail_prediction import RailPrediction
from metrodashboard.tools.logger import get_logger
from metrodashboard.cache.prediction_cache import TRAIN_CACHE
from metrodashboard.services.stations_service import StationsService
import json

class NextTrain:
    """
        Exposes methods to use the NextTrain API from WMATA
    """
    _BASE_PATH = 'StationPrediction.svc/json/'
    def __init__(self, client: MetroClient, stations: StationsService):
        self.client = client
        self._logger = get_logger(__name__)
        self._stations = stations.stations()
    
    def get_next_trains_for_station(self, station_name: str, line: str) -> list[RailPrediction]:
        station_code = self.stations[station_name][line]
        endpoint = f'{self._BASE_PATH}/GetPrediction/{station_code}'

        return [RailPrediction(prediction) for prediction in self.client.make_api_request(endpoint)['Trains']]

    def get_all_rail_predictions(self) -> list[RailPrediction]:
        endpoint = f'{self._BASE_PATH}/GetPrediction/All'

        return [RailPrediction(prediction) for prediction in self.client.make_api_request(endpoint)['Trains']]


        
