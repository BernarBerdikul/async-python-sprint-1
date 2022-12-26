from typing import Any

from tasks import (
    DataAggregationTask,
    DataAnalyzingTask,
    DataCalculationTask,
    DataFetchingTask,
)


def forecast_weather():
    """
    Анализ погодных условий по городам
    """
    print('Шаг 1. Запрашиваем данные о погоде по городам.')
    fetched_data: list[tuple[str, dict]] = DataFetchingTask().run()

    print('Шаг 2. Рассчитываем погодные данные по городам.')
    calculated_data: list[dict[str, Any]] = DataCalculationTask(
        fetched_data=fetched_data,
    ).run()

    print('Шаг 3. Находим лучшие города.')
    best_city = DataAnalyzingTask(calculated_data=calculated_data).run()

    print('Шаг 4. Сохраняем результат в json-файл.')
    DataAggregationTask(aggregated_data=best_city).run()


if __name__ == '__main__':
    forecast_weather()
