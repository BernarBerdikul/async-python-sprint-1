__all__ = ('DataAnalyzingTask',)

from dataclasses import dataclass, field
from typing import Any


@dataclass
class DataAnalyzingTask:
    """
    Класс для поиска лучших городов.
    """

    calculated_data: list[dict[str, Any]]
    max_rating: int = 0
    sorted_data: list = field(default_factory=list)

    def sort_data(self) -> None:
        """
        Метод для сортировки городов по рейтингу.
        """
        self.sorted_data = sorted(
            self.calculated_data,
            key=lambda x: x['rating'],
            reverse=True,
        )

    def set_max_rating(self) -> None:
        """
        Метод для установления максимального рейтинга по городам.
        """
        best_city = self.sorted_data[0]
        self.max_rating = best_city['rating']

    def analyze_data(self) -> list[dict[str, Any]]:
        """
        Метод для поиска лучших городов по максимальному рейтингу.
        """
        return [d for d in self.sorted_data if d['rating'] == self.max_rating]

    def run(self) -> list[dict[str, Any]]:
        """
        Метод для запуска сценария класса.
        """
        self.sort_data()
        self.set_max_rating()
        return self.analyze_data()
