from metrodashboard.api.metro import MetroClient
from metrodashboard.models.train_position import TrainPosition
from metrodashboard.models.track_circuit import TrackCircuit

class TrainPositions:
    __BASE_ENDPOINT = 'TrainPositions'
    def __init__(self, metro_client: MetroClient) -> None:
        self.client = metro_client
    
    def get_all_train_positions(self) -> list[TrainPosition]:
        api_response = self.client.make_api_request(f'{self.__BASE_ENDPOINT}/TrainPositions')
        positions = []
        for raw_position_data in api_response['TrainPositions']:
            positions.append(TrainPosition(raw_position_data))
        return positions

    def track_circuits(self) -> list[TrackCircuit]:
        endpoint = f'{self.__BASE_ENDPOINT}/TrackCircuits'
        return [TrackCircuit(circuit) for circuit in self.client.make_api_request(endpoint)['TrackCircuits']]
