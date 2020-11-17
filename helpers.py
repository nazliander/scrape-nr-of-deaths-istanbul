from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

from custom_logger import set_logger


LOGGER = set_logger("selenium_stats")


def get_death_from_record(record: str) -> str:
    """In the records, the second word implies the total number of
    deaths in a given day.
    """
    try:
        return record.split(" ")[1]
    except:
        return None


def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options


def take_death_number(date_str: str,
                      chrome_options: Options,
                      url: str) -> str:
    """Main function of the scraper.
    Takes the death numbers from the given webpage for
    official statistics.
    The web site might change in time. Hence, the operations applied in sequence:
    1. Find the element by ID in the given webpage with 'tarih'.
    2. Enter the date as text in the given element ID.
    3. Gets the text from the class element 'tablePagination'"""
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(800, 600)
        driver.get(url)
        time.sleep(5)
        date_element = driver.find_element_by_id("tarih")
        date_element.send_keys(date_str)
        date_element.send_keys(Keys.ENTER)
        time.sleep(5)
        pagination = driver.find_element_by_class_name("tablePagination")
        return pagination.text
    except Exception as shit:
        LOGGER.error(f"{shit} happened.")
        return None
    finally:
        driver.quit()
