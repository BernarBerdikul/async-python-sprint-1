__all__ = ('DataFetchingTask',)
import logging
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from typing import ClassVar

from clients.weather_api import YandexWeatherAPI
from utils import constants

logger = logging.getLogger(__name__)


@dataclass
class DataFetchingTask:
    """
    Класс для получения данных из API погоды.
    """

    WEATHER_API: ClassVar[YandexWeatherAPI] = YandexWeatherAPI()

    def fetch(self, city_name: str) -> tuple[str, dict]:
        """
        Метод для запроса данных по названию города.
        """
        logger.info(f'{city_name}: запрашиваем погоду в городе.')
        resp = self.WEATHER_API.get_forecasting(city_name=city_name)
        return city_name, resp

    def run(self) -> list[tuple[str, dict]]:
        with ThreadPoolExecutor() as pool:
            futures = [
                pool.submit(self.fetch, city_name=city)
                for city in constants.CITIES
            ]
            fetched_data: list[tuple[str, dict]] = [
                f.result()
                for f in futures
            ]
        return fetched_data
