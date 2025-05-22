from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from framework.drive_manager import DriverManager


class LoaderPageObjects:
    def __init__(self):
        self.driver: WebDriver = DriverManager.get_driver()

    def get_loader(self)-> WebElement:
        return self.driver.find_element(By.XPATH, '//div[@data-testid="uds-backdrop-component"]')