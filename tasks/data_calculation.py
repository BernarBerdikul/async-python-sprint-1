from dataclasses import dataclass, field
from typing import Any
from utils import constants


__all__ = ('DataCalculationTask',)


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
        return len([h for h in hours if h['condition'] in constants.WEATHER_WITHOUT_PRECIPITATION])

    def calculation(self) -> dict[str, dict[str, Any]]:
        week_day_temp: list[float] = []
        week_day_hours_without_precipitation: list[int] = []
        for forecast in self.forecasts:
            date = forecast['date']
            print(f"[{date}]{self.city_name}: Фильтруем часы между 9:00 и 19:00.")
            target_hours: list = [hour for hour in forecast['hours'] if 8 < int(hour['hour']) < 20]

            print(f"[{date}]{self.city_name}: Получаем данные по часам осадков.")
            hours_without_precipitation: int = self.count_hours_without_precipitation(hours=target_hours)
            week_day_hours_without_precipitation.append(hours_without_precipitation)

            print(f"[{date}]{self.city_name}: Получаем данные по температурам.")
            average_day_temp: str = "-"
            if target_hours:
                temp: float = self.average(data=[h['temp'] for h in target_hours])
                average_day_temp: str = str(temp)
                week_day_temp.append(temp)
            self.days.append(
                {
                    "date": date,
                    "hours_without_precipitation": hours_without_precipitation,
                    "average_day_temp": average_day_temp,
                }
            )
        return {
            self.city_name: {
                "city_name": self.city_name,
                "days": self.days,
                "average_week_temp": self.average(data=week_day_temp),
                "average_without_precipitation": self.average(data=week_day_hours_without_precipitation),
                "rating": "-",
                "forecasts": self.forecasts,
            }
        }

    def __call__(self, *args, **kwargs) -> dict[str, dict[str, Any]]:
        return self.calculation()
