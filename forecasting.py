import logging
from typing import Any

from tasks import (
    DataAggregationTask,
    DataAnalyzingTask,
    DataCalculationTask,
    DataFetchingTask,
)

logger = logging.getLogger(__name__)


def forecast_weather():
    """
    Анализ погодных условий по городам
    """
    logger.info('Шаг 1. Запрашиваем данные о погоде по городам.')
    fetched_data: list[tuple[str, dict]] = DataFetchingTask().run()

    logger.info('Шаг 2. Рассчитываем погодные данные по городам.')
    calculated_data: list[dict[str, Any]] = DataCalculationTask(
        fetched_data=fetched_data,
    ).run()

    logger.info('Шаг 3. Находим лучшие города.')
    best_city = DataAnalyzingTask(calculated_data=calculated_data).run()

    logger.info('Шаг 4. Сохраняем результат в json-файл.')
    DataAggregationTask(aggregated_data=best_city).run()


if __name__ == '__main__':
    forecast_weather()
