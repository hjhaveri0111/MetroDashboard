class StationToStationInfo:
    def __init__(self, raw_content) -> None:
        self.composite_miles = raw_content['CompositeMiles']
        self.destination_station = raw_content['DestinationStation']
        self.rail_fare = RailFare(raw_content['RailFare'])
        self.rail_time = raw_content['RailTime']
        self.source_station = raw_content['SourceStation']
    
    def __str__(self) -> str:
        return (
            f"StationToStationInfo("
            f"source_station={self.source_station}, "
            f"destination_station={self.destination_station}, "
            f"composite_miles={self.composite_miles}, "
            f"rail_time={self.rail_time}, "
            f"rail_fare={self.rail_fare}"
            f")"
        )

class RailFare:
    def __init__(self, raw_content) -> None:
        self.off_peak_time = raw_content['OffPeakTime']
        self.peak_time = raw_content['PeakTime']
        self.senior_disabled = raw_content['SeniorDisabled']

    def __str__(self) -> str:
        return (
            f"RailFare("
            f"off_peak_time={self.off_peak_time}, "
            f"peak_time={self.peak_time}, "
            f"senior_disabled={self.senior_disabled}"
            f")"
        )