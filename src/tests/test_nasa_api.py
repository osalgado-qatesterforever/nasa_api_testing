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
        apod_endpoint = "planetary/apod"
        this_function_name = inspect.stack()[0].function
        
        response = api_client.get(apod_endpoint)
        pp = PrettyPrinter()
        response.raise_for_status()
        log.info(f"Test {this_function_name } passed.")
        log.info(f"Pretty response:\n {pp.pformat(response.json())}")
        

