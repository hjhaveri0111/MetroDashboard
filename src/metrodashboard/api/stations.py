from metrodashboard.models.station import Station
from metrodashboard.api.metro import MetroClient
class Stations:
    _BASE_PATH = 'Rail.svc/json'
    def __init__(self, client: MetroClient) -> None:
        self.client = client
    
    def list_all_stations(self) -> list[Station]:
        endpoint = f'{self._BASE_PATH}/jStations'
        response = self.client.make_api_request(endpoint)

        return [Station(station) for station in response['Stations']]