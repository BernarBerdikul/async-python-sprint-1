from tasks import DataFetchingTask


def test_data_fetching():
    city_name_for_test: str = 'BERLIN'
    resp_city_name, resp_data = DataFetchingTask().fetch(city_name=city_name_for_test)
    assert resp_city_name == city_name_for_test
