from clients.weather_api import YandexWeatherAPI


def check_api():
    city_name_for_test: str = "MOSCOW"

    yw_api = YandexWeatherAPI()
    resp = yw_api.get_forecasting(city_name=city_name_for_test)
    attr = resp.get("info")
    print(attr)
