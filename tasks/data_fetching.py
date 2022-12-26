__all__ = ('DataFetchingTask',)

from dataclasses import dataclass
from typing import ClassVar

from clients.weather_api import YandexWeatherAPI


@dataclass
class DataFetchingTask:
    """
    Класс для получения данных из API погоды.
    """

    city_name: str
    WEATHER_API: ClassVar[YandexWeatherAPI] = YandexWeatherAPI()

    def fetch(self) -> tuple[str, dict]:
        """
        Метод для запроса данных по названию города.
        """
        print(f'{self.city_name}: запрашиваем погоду в городе.')
        resp = self.WEATHER_API.get_forecasting(city_name=self.city_name)
        return self.city_name, resp

    def __call__(self, *args, **kwargs) -> tuple[str, dict]:
        """
        Определяем метод класса, для вызова как функцию.
        """
        return self.fetch()
