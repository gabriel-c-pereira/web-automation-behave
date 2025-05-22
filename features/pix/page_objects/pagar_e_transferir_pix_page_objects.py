from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from framework.drive_manager import DriverManager


class PagarETransferirPixPageObjects:
    def __init__(self):
        self.driver: WebDriver = DriverManager.get_driver()

    def get_transferir_com_chave_pix_button(self)-> WebElement:
        return self.driver.find_element(By.XPATH, '//*[@data-testid="UdsKeyIcon"]')