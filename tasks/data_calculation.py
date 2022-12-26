from dataclasses import dataclass, field
from typing import Any

from utils import constants

__all__ = ('DataCalculationTask',)


# Рейтинг по осадкам
PRECIPITATION_RATING: dict[int, list[int]] = {
    1: [1, 2],
    2: [3, 4],
    3: [5, 6],
    4: [7, 8],
    5: [9, 10],
}

# Рейтинг по температуре
TEMP_RATING: dict[int, list[int]] = {
    1: [0, 5],
    2: [5, 10],
    3: [10, 20],
    4: [20, 30],
    5: [30, 40],
}


@dataclass
class DataCalculationTask:
    """
    Класс для расчёта информаций о городе.
    """

    city_name: str
    forecasts: list[dict[str, Any]]
    days: list = field(default_factory=list)

    @staticmethod
    def average(data: list[Any]) -> float:
        """
        Метод для подсчёта среднего арифметического значения.
        """
        return round(sum(data) / len(data), 1)

    @staticmethod
    def count_hours_without_precipitation(hours: list) -> int:
        """
        Метод для подсчёта кол-ва часов без осадков.
        """
        return len(
            [
                h
                for h in hours
                if h['condition'] in constants.WEATHER_WITHOUT_PRECIPITATION
            ],
        )

    @staticmethod
    def calculate_rating(
        average_week_temp: float,
        average_without_precipitation: float,
    ) -> int:
        """
        Метод для расчёта рейтинга города, в зависимости от погоды и температуры.
        """
        rating: int = 0
        for rate, (l_p_border, r_p_border) in PRECIPITATION_RATING.items():
            if l_p_border <= average_without_precipitation <= r_p_border:
                rating += rate
                break
        for rate, (l_t_border, r_t_border) in TEMP_RATING.items():
            if l_t_border < average_week_temp <= r_t_border:
                rating += rate
                break
        return rating

    @staticmethod
    def filter_target_hours(hours: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """
        Метод для фильтраций часов в период с 9:00 по 19:00.
        """
        return [
            hour for hour in hours if 8 < int(hour['hour']) < 20
        ]

    def calculation(self) -> dict[str, Any]:
        """
        Метод для расчёта данных температуры и погоды в городе.
        """
        wday_temp: list[float] = []
        wday_hours_without_precipitation: list[int] = []
        for forecast in self.forecasts:
            date = forecast['date']
            print(f'[{date}]{self.city_name}: Фильтруем часы между 9:00 и 19:00.')
            target_hours: list[dict[str, Any]] = self.filter_target_hours(
                hours=forecast['hours'],
            )
            print(f'[{date}]{self.city_name}: Получаем данные по часам осадков.')
            h_without_precipitation: int = self.count_hours_without_precipitation(
                hours=target_hours,
            )
            wday_hours_without_precipitation.append(h_without_precipitation)

            print(f'[{date}]{self.city_name}: Получаем данные по температурам.')
            average_day_temp: str = '-'
            if target_hours:
                temp: float = self.average(
                    data=[h['temp'] for h in target_hours],
                )
                average_day_temp = str(temp)
                wday_temp.append(temp)
            self.days.append(
                {
                    'date': date,
                    'hours_without_precipitation': h_without_precipitation,
                    'average_day_temp': average_day_temp,
                },
            )
        average_week_temp: float = self.average(data=wday_temp)
        average_without_precipitation: float = self.average(
            data=wday_hours_without_precipitation,
        )
        rating: int = self.calculate_rating(
            average_week_temp=average_week_temp,
            average_without_precipitation=average_without_precipitation,
        )
        print(f'[{self.city_name}]: Получен рейтинг города = {rating}.')
        return {
            'city_name': self.city_name,
            'days': self.days,
            'average_week_temp': average_week_temp,
            'average_without_precipitation': average_without_precipitation,
            'rating': rating,
            'forecasts': self.forecasts,
        }

    def __call__(self, *args, **kwargs) -> dict[str, Any]:
        """
        Определяем метод класса, для вызова как функцию.
        """
        return self.calculation()
