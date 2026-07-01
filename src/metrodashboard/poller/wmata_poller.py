import asyncio
from metrodashboard.cache.prediction_cache import TRAIN_CACHE
from metrodashboard.api.next_train import NextTrain
from metrodashboard.models.rail_prediction import RailPrediction
from metrodashboard.tools.logger import get_logger
from datetime import datetime

class WmataPoller:
    def __init__(self, client: NextTrain, interval_seconds: int = 20) -> None:
        self._client = client
        self._interval = interval_seconds
        self._logger = get_logger(__name__)

    def _group_by_station(self, trains: list[RailPrediction]) -> dict:
        grouped = {}

        for t in trains:
            code = t.location_code
            if not code:
                continue

            grouped.setdefault(code, []).append(t)

        return grouped

    async def run(self):
        while True:
            try:
                self._logger.info("Querying WMATA for all station predictions")
                data = self._client.get_all_rail_predictions()

                self._logger.info("Successfully queried WMATA")
                grouped = self._group_by_station(data)


                TRAIN_CACHE.update({
                    "grouped": grouped,
                    "last_updated": datetime.utcnow()
                })
                self._logger.info("Successfully cached")

            except Exception as e:
                self._logger.exception("WMATA fetch failed")

            await asyncio.sleep(self._interval)