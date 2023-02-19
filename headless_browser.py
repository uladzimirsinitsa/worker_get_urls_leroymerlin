
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions


def get_data_from_url(url: str):
    service = Service(executable_path=r'/usr/src/app/chromedriver')
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument("--incognito")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    driver.set_window_size(1920, 1080)
    time.sleep(3)
    return driver.page_source
