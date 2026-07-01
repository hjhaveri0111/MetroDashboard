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
    
    def __str__(self) -> str:
        return(
            f"Car: {self.car} "
            f"Destination: {self.destination} "
            f"Destination_Code: {self.destination_code} "
            f"Destination_Name: {self.destination_name} "
            f"Group: {self.group} "
            f"Line: {self.line} "
            f"Location_Code: {self.location_code} "
            f"Location_Name: {self.location_name} "
            f"Min: {self.min} "
        )