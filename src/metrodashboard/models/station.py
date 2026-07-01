class Station:
    def __init__(self, raw_content) -> None:
        self.address = raw_content['Address']
        self.code = raw_content['Code']
        self.lat = raw_content['Lat']
        self.line_code1 = raw_content['LineCode1']
        self.line_code2 = raw_content['LineCode2']
        self.line_code3 = raw_content['LineCode3']
        self.line_code4 = raw_content['LineCode4']
        self.lon = raw_content['Lon']
        self.name = raw_content['Name']
        self.station_together1 = raw_content['StationTogether1']
        self.station_together2 = raw_content['StationTogether2']
    def __str__(self):
        return (
            f"Station("
            f"address={self.address}, "
            f"code={self.code}, "
            f"lat={self.lat}, "
            f"line_code1={self.line_code1}, "
            f"line_code2={self.line_code2}, "
            f"line_code3={self.line_code3}, "
            f"line_code4={self.line_code4}, "
            f"lon={self.lon}, "
            f"name={self.name}, "
            f"station_together1={self.station_together1}, "
            f"station_together2={self.station_together2}"
            f")"
        )