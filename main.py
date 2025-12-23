import json
import os

from metrodashboard.api.train_positions import TrainPositions
from metrodashboard.api.stations import Stations
from metrodashboard.api.next_train import NextTrain
from metrodashboard.api.metro import MetroClient
from dotenv import load_dotenv

load_dotenv()
def main():
    print("Hello from metrodashboard!")
    client = MetroClient()
    positions = TrainPositions(client)
    response = positions.get_all_train_positions()
    next_train = NextTrain(client)
    predictions = next_train.get_next_trains_for_station('Pentagon City')
    for prediction in predictions: 
        print(f'{prediction.destination}({prediction.destination_code}) coming in {prediction.min}')
    
    if bool(os.getenv("REFRESH")):
        refresh_station_codes()

def refresh_station_codes(client: MetroClient):
    stations = Stations(client)
    all_stations = {station.name: station.code for station in stations.list_all_stations()}
    with open('stations.json', 'w') as f:
        json.dump(all_stations, f, indent=4) 



if __name__ == "__main__":
    main()
