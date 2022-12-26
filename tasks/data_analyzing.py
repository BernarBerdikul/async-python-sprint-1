__all__ = ('DataAnalyzingTask',)

import json
from dataclasses import dataclass, field
from typing import Any

from utils import constants


@dataclass
class DataAnalyzingTask:
    """
    Класс для поиска лучших городов.
    """

    max_rating: int = 0
    aggregated_data: list = field(default_factory=list)
    sorted_data: list = field(default_factory=list)

    def read_file(self):
        """
        Метод для загрузки результатов из файла.
        """
        with open(constants.RESULT_FILE) as f:
            self.aggregated_data = json.loads(f.read())

    def sort_data(self) -> None:
        """
        Метод для сортировки городов по рейтингу.
        """
        self.sorted_data = sorted(
            self.aggregated_data,
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
        self.read_file()
        self.sort_data()
        self.set_max_rating()
        result = self.analyze_data()
        return result
