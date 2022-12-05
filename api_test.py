def check_python_version():
    from utils import check_python_version

    check_python_version()


def check_api():
    from api_client import YandexWeatherAPI

    city_name_for_test: str = "MOSCOW"

    yw_api = YandexWeatherAPI()
    resp = yw_api.get_forecasting(city_name=city_name_for_test)
    attr = resp.get("info")
    print(attr)


if __name__ == "__main__":
    check_python_version()
    check_api()
