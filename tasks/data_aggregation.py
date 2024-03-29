import json
import logging
from dataclasses import dataclass
from typing import Any

from utils import constants

__all__ = ('DataAggregationTask',)

logger = logging.getLogger(__name__)


@dataclass
class DataAggregationTask:
    """
    Класс для сохранения результата расчётов.
    """

    aggregated_data: list[dict[str, Any]]

    def _save_in_file(self) -> None:
        """
        Метод для сохранения результата в json-файл.
        """
        logger.info(f'Сохраняем результат в файл {constants.RESULT_FILE}')
        payload = json.dumps(
            self.aggregated_data,
            ensure_ascii=False, indent=4,
        )
        with open(constants.RESULT_FILE, 'w') as f:
            f.write(payload)

    def run(self):
        """
        Метод для запуска сценария класса.
        """
        self._save_in_file()
