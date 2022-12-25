import json
from dataclasses import dataclass, field
from collections import ChainMap
from typing import Any
from utils import constants

__all__ = ('DataAggregationTask',)


@dataclass
class DataAggregationTask:
    calculated_data: list[dict[str, Any]]
    aggregated_data: dict = field(default_factory=dict)

    def _aggregate_data(self):
        self.aggregated_data = dict(ChainMap(*self.calculated_data))

    def _save_in_file(self) -> None:
        print(f"Сохраняем результат в файл {constants.RESULT_FILE}")
        payload = json.dumps(self.aggregated_data)
        with open(constants.RESULT_FILE, 'w') as f:
            f.write(payload)

    def run(self):
        self._aggregate_data()
        self._save_in_file()

