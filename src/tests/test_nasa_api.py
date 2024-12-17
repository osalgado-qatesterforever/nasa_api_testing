from src.utils.api_client import APIClient
from urllib.request import urlretrieve
from pprint import PrettyPrinter
import inspect
import pytest


@pytest.fixture(scope="module")
def api_client():
    return APIClient()


class TestNasa:
    def test_pic_of_the_day(self, api_client, log):
        apod_endpoint = "/planetary/apod"
        
        response = api_client.get(apod_endpoint)
        response.raise_for_status()
        pp = PrettyPrinter()
        log.info(f"Test {inspect.stack()[0].function } passed.")
        log.info(f"Pretty response:\n {pp.pformat(response.json())}")
    
    def test_near_earth_objects(self, api_client, log):
        neofeed_endpoint = "/neo/rest/v1/feed"
        params = {
            'start_date':'2020-01-22',
            'end_date':'2020-01-23'
        }
        response = api_client.get(neofeed_endpoint)
        response.raise_for_status()
        pp = PrettyPrinter()
        log.info(f"Test {inspect.stack()[0].function } passed.")
        log.info(f"Pretty response:\n {pp.pformat(response.json())}")

