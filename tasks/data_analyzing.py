
__all__ = ('DataAnalyzingTask',)

import json
from dataclasses import dataclass, field
from typing import Any

from utils import constants


@dataclass
class DataAnalyzingTask:
    max_rating: int = 0
    aggregated_data: list = field(default_factory=list)
    sorted_data: list = field(default_factory=list)

    def read_file(self):
        with open(constants.RESULT_FILE, 'r') as f:
            self.aggregated_data = json.loads(f.read())

    def sort_data(self) -> None:
        self.sorted_data = sorted(self.aggregated_data, key=lambda x: x['rating'], reverse=True)

    def set_max_rating(self) -> None:
        self.max_rating = max(self.sorted_data, key=lambda x: x['rating'])['rating']

    def analyze_data(self) -> list[dict[str, Any]]:
        return [
            d for d in self.sorted_data if d['rating'] == self.max_rating
        ]

    def run(self) -> list[dict[str, Any]]:
        self.read_file()
        self.sort_data()
        self.set_max_rating()
        result = self.analyze_data()
        return result
