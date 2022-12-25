from tasks import DataCalculationTask


def test_precipitation_counter(fetched_data_setup):
    resp_city_name, resp_data = fetched_data_setup
    target_hours: list = DataCalculationTask.filter_target_hours(
        hours=resp_data['forecasts'][0]['hours'],
    )
    h_without_precipitation: int = DataCalculationTask.count_hours_without_precipitation(
        hours=target_hours,
    )
    assert isinstance(h_without_precipitation, int)
