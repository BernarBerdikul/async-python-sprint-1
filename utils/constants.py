CITIES: dict[str, str] = {
    'MOSCOW': 'https://code.s3.yandex.net/async-module/moscow-response.json',
    'PARIS': 'https://code.s3.yandex.net/async-module/paris-response.json',
    'LONDON': 'https://code.s3.yandex.net/async-module/london-response.json',
    'BERLIN': 'https://code.s3.yandex.net/async-module/berlin-response.json',
    'BEIJING': 'https://code.s3.yandex.net/async-module/beijing-response.json',
    'KAZAN': 'https://code.s3.yandex.net/async-module/kazan-response.json',
    'SPETERSBURG': 'https://code.s3.yandex.net/async-module/spetersburg-response.json',
    'VOLGOGRAD': 'https://code.s3.yandex.net/async-module/volgograd-response.json',
    'NOVOSIBIRSK': 'https://code.s3.yandex.net/async-module/novosibirsk-response.json',
    'KALININGRAD': 'https://code.s3.yandex.net/async-module/kaliningrad-response.json',
    'ABUDHABI': 'https://code.s3.yandex.net/async-module/abudhabi-response.json',
    'WARSZAWA': 'https://code.s3.yandex.net/async-module/warszawa-response.json',
    'BUCHAREST': 'https://code.s3.yandex.net/async-module/bucharest-response.json',
    'ROMA': 'https://code.s3.yandex.net/async-module/roma-response.json',
    'CAIRO': 'https://code.s3.yandex.net/async-module/cairo-response.json',
}
WEATHER_WITHOUT_PRECIPITATION: list[str] = [
    'clear',
    'partly',
    'cloudy',
    'overcast',
]
RESULT_FILE: str = 'result.json'

ERR_MESSAGE_TEMPLATE: str = 'Something wrong. Please contact with mentor.'

MIN_MAJOR_PYTHON_VER: int = 3
MIN_MINOR_PYTHON_VER: int = 9
