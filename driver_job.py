# pip install python-dotenv
# pip install webdriver-manager
import sys

from dotenv import load_dotenv
import os
from selenium.webdriver import FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from time_zone import get_city_time
import re
from loguru import logger

# custom_formatter = "<red>{time:YYYY-MM-DD HH:mm}</red> | <level>{level}</level> | <cyan>{message}</cyan>"
# logger.add(sink="stdout",format=custom_formatter)

service = Service(GeckoDriverManager().install())
options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(service=service, options=options)


def find_date(str_with_date='№24 Пн, 25.02.24'):
    re_pattern = r'\d{2}\.\d{2}\.\d{2}'
    return re.findall(re_pattern, str_with_date)[0]


def get_today_link(all_spans):
    today = get_city_time('Europe/Moscow').strftime("%d.%m.%y")
    for span in all_spans:
        if find_date(span.text) == today:
            today_link = span.get_attribute('href')
            return today_link


def get_spans():
    load_dotenv()
    rdk_logging = os.environ.get('rdk_logging')
    driver.get(rdk_logging)
    driver.get('https://rdk.spb.kommersant.ru:9443/rdk2/?p=RDK2SPB,NODE:2353975')
    all_spans = driver.find_elements('xpath', '//span[@id="phList"]/a')
    logger.info(f"{len(all_spans)}")
    return all_spans


def get_work_map():
    all_spans = get_spans()
    today_link = get_today_link(all_spans)
    driver.get(today_link)  # '//tr[@class="mapLO"][2]/td[6]/img'
    work_map = driver.find_elements('xpath', '//tr[@class="mapLO"]')
    driver.quit()
    return work_map


if __name__ == '__main__':
    get_work_map()
