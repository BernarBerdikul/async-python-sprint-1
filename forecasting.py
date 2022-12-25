from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from typing import Any

from tasks import (
    DataAggregationTask,
    DataAnalyzingTask,
    DataCalculationTask,
    DataFetchingTask,
)
from utils import constants


def forecast_weather():
    """
    Анализ погодных условий по городам
    """
    with ThreadPoolExecutor() as pool:
        futures = [pool.submit(DataFetchingTask(city_name=city)) for city in constants.CITIES]
        fetched_data: list[tuple[str, dict]] = [f.result() for f in futures]

    with ProcessPoolExecutor() as pool:
        futures = [
            pool.submit(DataCalculationTask(city_name=city_name, forecasts=result['forecasts']))
            for city_name, result in fetched_data
        ]
        calculated_data: list[dict[str, Any]] = [f.result() for f in futures]

    DataAggregationTask(aggregated_data=calculated_data).run()
    best_city = DataAnalyzingTask().run()
    print(best_city)


if __name__ == "__main__":
    forecast_weather()
