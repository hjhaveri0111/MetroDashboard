class TrainPosition: 
    def __init__(self, raw_json) -> None:
        self.car_count = raw_json.get('CarCount', None)
        self.circuit_id = raw_json.get('CircuitId', None)
        self.destination_station_code = raw_json.get('DestinationStationCode', None)
        self.direction_num = raw_json.get('DirectionNum', None)
        self.line_code = raw_json.get('LineCode', None)
        self.seconds_at_location = raw_json.get('SecondsAtLocation', None)
        self.service_type = raw_json.get('ServiceType', None)
        self.train_id = raw_json.get('TrainId', None)
        self.train_number = raw_json.get('TrainNumber', None)
        self.service = raw_json.get('Service', None)
        self.service_type = raw_json.get('ServiceType', None)