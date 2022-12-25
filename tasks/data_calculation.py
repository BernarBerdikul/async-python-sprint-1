from dataclasses import dataclass, field
from typing import Any

from utils import constants

__all__ = ('DataCalculationTask',)


PRECIPITATION_RATING: dict[int, list[int]] = {
    1: [1, 2],
    2: [3, 4],
    3: [5, 6],
    4: [7, 8],
    5: [9, 10],
}


TEMP_RATING: dict[int, list[int]] = {
    1: [0, 5],
    2: [5, 10],
    3: [10, 30],
    4: [20, 30],
    5: [30, 40],
}


@dataclass
class DataCalculationTask:
    city_name: str
    forecasts: list[dict[str, Any]]
    days: list = field(default_factory=list)

    @staticmethod
    def average(data: list[Any]) -> float:
        return round(sum(data) / len(data), 1)

    @staticmethod
    def count_hours_without_precipitation(hours: list) -> int:
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
        average_week_temp_rating: int = 0
        average_without_precipitation_rating: int = 0
        for rate, (l_border, r_border) in PRECIPITATION_RATING.items():
            if average_without_precipitation == 0:
                break
            if l_border < average_without_precipitation <= r_border:
                average_without_precipitation_rating = rate
                break
        for rate, (l_border, r_border) in TEMP_RATING.items():
            if average_week_temp == 0:
                break
            if l_border < average_week_temp <= r_border:
                average_week_temp_rating = rate
                break
        rating = average_week_temp_rating + average_without_precipitation_rating
        return rating

    def calculation(self) -> dict[str, Any]:
        week_day_temp: list[float] = []
        week_day_hours_without_precipitation: list[int] = []
        for forecast in self.forecasts:
            date = forecast['date']
            print(f'[{date}]{self.city_name}: Фильтруем часы между 9:00 и 19:00.')
            target_hours: list = [
                hour for hour in forecast['hours'] if 8 < int(hour['hour']) < 20
            ]

            print(f'[{date}]{self.city_name}: Получаем данные по часам осадков.')
            hours_without_precipitation: int = self.count_hours_without_precipitation(
                hours=target_hours,
            )
            week_day_hours_without_precipitation.append(
                hours_without_precipitation,
            )

            print(f'[{date}]{self.city_name}: Получаем данные по температурам.')
            average_day_temp: str = '-'
            if target_hours:
                temp: float = self.average(
                    data=[h['temp'] for h in target_hours],
                )
                average_day_temp = str(temp)
                week_day_temp.append(temp)
            self.days.append(
                {
                    'date': date,
                    'hours_without_precipitation': hours_without_precipitation,
                    'average_day_temp': average_day_temp,
                },
            )
        average_week_temp: float = self.average(data=week_day_temp)
        average_without_precipitation: float = self.average(
            data=week_day_hours_without_precipitation,
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
        return self.calculation()
