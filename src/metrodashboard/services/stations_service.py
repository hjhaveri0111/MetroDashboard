import json

class StationsService:
    """
        Wrapper class to provide access to the stations.json file. 
        This will be the main load point and all other classes that 
        need to reference data in this file can do so via this class
    """
    def __init__(self) -> None:
        with open('stations.json', 'r') as f:
            self._stations = json.load(f)

    def get_lines_for_station(self, station_name: str):
        return self._stations.get(station_name, {})
    
    def stations(self):
        return self._stations
    
    def get_station_codes(self, station_name):
        return self._stations.get(station_name, {}).values()