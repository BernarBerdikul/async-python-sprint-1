from tasks import DataCalculationTask


def test_data_calculation(fetched_data_setup):
    resp_city_name, resp_data = fetched_data_setup
    calculated_data = DataCalculationTask(fetched_data=[fetched_data_setup]).calculation(
        city_name=resp_city_name,
        forecasts=resp_data['forecasts'],
    )
    assert calculated_data['city_name'] == resp_city_name
    assert len(calculated_data['days']) == 5
    assert len(calculated_data['forecasts']) == 5
    assert 0 <= calculated_data['rating'] <= 10
