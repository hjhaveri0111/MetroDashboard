from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from enum import Enum
import asyncio

from metrodashboard.api.stations import Stations
from metrodashboard.api.next_train import NextTrain
from metrodashboard.api.metro import MetroClient
from metrodashboard.poller.wmata_poller import WmataPoller
from metrodashboard.services.station_predictions import StationPredictions
from metrodashboard.services.stations_service import StationsService
from dotenv import load_dotenv
load_dotenv()

"""
What are my customer access patterns

Given a station name and a line, give me the station predictions

I will resolve the backend for thi
"""
class Prediction(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    line: str
    destination: str
    car: str
    min: str
    group: str

class Line(str, Enum):
    blue = 'BL'
    yellow = 'YL'
    red = 'RD'
    orange = 'OR'
    silver = 'SV'
    green = 'GR'

client = MetroClient()
stations_service = StationsService()
next_train = NextTrain(client, stations_service)
stations = Stations(client)
predictions = StationPredictions(stations_service)

@asynccontextmanager
async def lifespan(app: FastAPI):
    poller = WmataPoller(next_train, interval_seconds=20)
    asyncio.create_task(poller.run())
    yield
    
app = FastAPI(lifespan=lifespan)

@app.get("/")
def landing_page():
    return "Hello from Metro Dashboard"

@app.get("/station/{station_name}")
def get_station_predictions(station_name: str):
    return {
        "station": station_name,
        "predictions": predictions.get_predictions_for_station(station_name)
    }

@app.get("/stations")
def get_stations():
    return [
        {
            "name": name,
            "lines": list(lines.keys())
        }
        for name, lines in stations.list_all_stations_cached().items()
    ]