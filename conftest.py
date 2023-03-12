import json
import pytest
import logging
import allure
import requests
from faker import Faker
from selenium import webdriver
from string import ascii_uppercase
from API_tests_data import api_key, api_username
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser",
                     default="chrome")
    parser.addoption("--headless",
                     action="store_true")
    parser.addoption("--base_url",
                     default="http://192.168.0.74:8081")
    parser.addoption("--remote_url",
                     default="http://192.168.0.74")
    parser.addoption("--log_level",
                     action="store",
                     default="DEBUG")
    parser.addoption("--machine",
                     default="local",
                     choices=["local", "remote"])
    parser.addoption("--bv",
                     action="store")
    parser.addoption("--vnc",
                     action="store_true")
    parser.addoption("--logs",
                     action="store_true")
    parser.addoption("--video",
                     action="store_true")


@allure.step("Getting fake user {data_name}")
def get_data(data_name):
    fake = Faker()
    if data_name == "firstname":
        firstname = fake.first_name()
        return firstname
    elif data_name == "lastname":
        lastname = fake.last_name()
        return lastname
    elif data_name == "address":
        address = fake.address()
        return address
    elif data_name == "city":
        city = fake.city()
        return city
    elif data_name == "country_id":
        country_id = fake.country()
        return country_id
    elif data_name == "zone_id":
        zone_id = ''.join(fake.random.choices(ascii_uppercase, k=3))
        return zone_id
    

@pytest.fixture
def api_session():
    api_session = requests.Session()
    return api_session


@pytest.fixture
def api_token(base_url, api_session):
    api_token = json.loads(api_session.post(
        f'{base_url}/index.php?route=api/login',
        data={'username': api_username,
              'key': api_key}
        ).text)['api_token']
    return api_token


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")
    machine = request.config.getoption("--machine")
    executor = request.config.getoption("--remote_url")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info(f"======> Test {request.node.name} started")

    if machine == "local":

        if _browser == "firefox":
            options = FirefoxOptions()
            options.headless = headless
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()), options=options
            )
        elif _browser == "chrome":
            options = ChromeOptions()
            options.headless = headless
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()), options=options
            )

    elif machine == "remote":
        if _browser == "chrome":
            options = ChromeOptions()
        elif _browser == "firefox":
            options = FirefoxOptions()
        _version = request.config.getoption("--bv")
        vnc = request.config.getoption("--vnc")
        video = request.config.getoption("--video")
        driver = webdriver.Remote(
            command_executor=f"{executor}:4444/wd/hub",
            desired_capabilities={"browserName": _browser,
                                  "browserVersion": _version,
                                  "selenoid:options": {
                                      "screenResolution": "1285x720",
                                      "name": "OTUS_homework_11",
                                      "enableVNC": vnc,
                                      "enableVideo": video
                                        }
                                  },
            options=options
        )

    logger.info(f"Browser:{_browser}")

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    driver.maximize_window()

    yield driver

    logger.info(f"======> Test {request.node.name} finished")

    driver.quit()
