# import logging
# import threading
# import subprocess
# import multiprocessing

from api_client import YandexWeatherAPI
from tasks import (
    DataAggregationTask,
    DataAnalyzingTask,
    DataCalculationTask,
    DataFetchingTask,
)
from utils import CITIES


def forecast_weather():
    """
    Анализ погодных условий по городам
    """
    # city_name = "MOSCOW"
    # yw_api = YandexWeatherAPI()
    # resp = yw_api.get_forecasting(city_name)
    pass


if __name__ == "__main__":
    forecast_weather()
