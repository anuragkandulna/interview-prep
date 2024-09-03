import time
from utils.custom_logger import CustomLogger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Invoke Logger
LOGGER = CustomLogger(__name__, level=20).get_logger()


def selenium_chrome(url):
    """Get selenium chrome driver for url."""
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def main():
    """
    Main function starts here.

    Link 1: https://rahulshettyacademy.com/AutomationPractice/
    Link 2: https://rahulshettyacademy.com/angularpractice/
    """
    driver = selenium_chrome(url="https://rahulshettyacademy.com/angularpractice/")
    LOGGER.info(driver)
    time.sleep(2)

    title = driver.title
    url = driver.current_url
    LOGGER.info(f"Title of page: {title}")
    LOGGER.info(f"URL of page: {url}")

    assert "ProtoCommerce" in title
    time.sleep(10)


if __name__ == '__main__':
    main()