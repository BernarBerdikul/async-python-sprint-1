import http
import logging
import json
from urllib.request import urlopen

from utils import constants

logger = logging.getLogger()

__all__ = ("YandexWeatherAPI",)


class YandexWeatherAPI:
    """Base class for requests."""

    @staticmethod
    def _do_req(url):
        """Base request method."""
        try:
            with urlopen(url=url) as req:
                resp = req.read().decode("utf-8")
                resp = json.loads(resp)
            if req.status != http.HTTPStatus.OK:
                raise Exception(f"Error during execute request. {resp.status}: {resp.reason}")
            return resp
        except Exception as ex:
            logger.error(ex)
            raise Exception(constants.ERR_MESSAGE_TEMPLATE)

    @staticmethod
    def _get_url_by_city_name(city_name: str) -> str:
        try:
            return constants.CITIES[city_name]
        except KeyError:
            raise Exception("Please check that city {} exists".format(city_name))

    def get_forecasting(self, city_name: str):
        """
        :param city_name: key as str
        :return: response data as json
        """
        city_url = self._get_url_by_city_name(city_name=city_name)
        return self._do_req(url=city_url)
