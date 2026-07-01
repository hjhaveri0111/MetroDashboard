from metrodashboard.cache.prediction_cache import TRAIN_CACHE
from metrodashboard.models.rail_prediction import RailPrediction
from metrodashboard.services.stations_service import StationsService
from metrodashboard.tools.logger import get_logger

class StationPredictions:
    def __init__(self, stations_service: StationsService) -> None:
        self._logger = get_logger(__name__)
        self._stations_service = stations_service

    def get_predictions_for_station(self, station_name) -> list[RailPrediction]:
        self._logger.info("Attempting to get predictions from station %s", station_name)
        lines = self._stations_service.get_lines_for_station(station_name)

        if not lines:
                self._logger.warning(
                    "Station not found: %s",
                    station_name
                )
                return []
        # collect unique station codes
        codes = set(lines.values())

        predictions = []

        for code in codes:
            predictions.extend(
                TRAIN_CACHE["grouped"].get(code, [])
            )

        return predictions