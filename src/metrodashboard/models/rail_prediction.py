class RailPrediction:
    def __init__(self, raw_content) -> None:
        self.car = raw_content['Car']
        self.destination = raw_content['Destination']
        self.destination_code = raw_content['DestinationCode']
        self.destination_name = raw_content['DestinationName']
        self.group = raw_content['Group']
        self.line = raw_content['Line']
        self.location_code = raw_content['LocationCode']
        self.location_name = raw_content['LocationName']
        self.min = raw_content['Min']