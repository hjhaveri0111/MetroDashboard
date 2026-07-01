import json 

from metrodashboard.models.station import Station
from metrodashboard.models.station_to_station_info import StationToStationInfo
from metrodashboard.api.metro import MetroClient

class Stations:
    """
    Class that is meant to represent the Stations endpoint in the WMATA API
    """
    _BASE_PATH = 'Rail.svc/json'
    def __init__(self, client: MetroClient) -> None:
        self.client = client
        with open('stations.json', 'r') as f:
            self.stations = json.load(f)
    
    def list_all_stations_cached(self):
        return self.stations
        
    def list_all_stations(self) -> list[Station]:
        """
        Get a list of all stations and their properties
        """
        endpoint = f'{self._BASE_PATH}/jStations'
        response = self.client.make_api_request(endpoint)

        return [Station(station) for station in response['Stations']]
    
    def get_station_information(self, station_name: str) -> Station:
        station_code = None

        station_code = self.stations[station_name]
        print(station_code)
        endpoint = f'{self._BASE_PATH}/jStationInfo?StationCode={station_code}'
        print(endpoint)
        print(self.client.make_api_request(endpoint))
        return Station(self.client.make_api_request(endpoint))
    
    def station_to_station_info(self, start_station: str, destination_station: str, line: str) -> list[StationToStationInfo]:
        """
        Get information such as rail time, fares, etc. for a station to station travel. 

        Args:
            start_station (str): Name of the station you are starting from.
            destination_station (str): Name of the station you wish to go to.

        Returns:
            list[StationToStationInfo]: List of information about the trip between the two stations.
        """
        start_station_code = None
        destination_station_code = None

        start_station_code = self.stations[start_station][line]
        destination_station_code = self.stations[destination_station][line]
        
        endpoint = f'{self._BASE_PATH}/jSrcStationToDstStationInfo?FromStationCode={start_station_code}&ToStationCode={destination_station_code}'

        return [StationToStationInfo(info) for info in self.client.make_api_request(endpoint)['StationToStationInfos']]
        