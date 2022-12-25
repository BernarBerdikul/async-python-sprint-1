import pytest

from tasks import DataFetchingTask


@pytest.fixture
def fetched_data_setup() -> tuple[str, dict]:
    city_name_for_test: str = 'BEIJING'
    resp_city_name, resp_data = DataFetchingTask(
        city_name=city_name_for_test,
    )()
    return resp_city_name, resp_data
