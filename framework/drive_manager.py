from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DriverManager:
    _driver: WebDriver|None = None

    @classmethod
    def get_driver(cls)-> WebDriver:
        if cls._driver is None:
            cls.__create_driver()
        return cls._driver

    @classmethod
    def quit_driver(cls)-> None:
        if cls._driver:
            cls._driver.quit()
            cls._driver = None

    @classmethod
    def __create_driver(cls)-> None:
        opt = webdriver.ChromeOptions()
        opt.add_argument("--headless")
        cls._driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)