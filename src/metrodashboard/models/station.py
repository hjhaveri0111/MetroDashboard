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