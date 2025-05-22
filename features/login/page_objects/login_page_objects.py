from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from framework.drive_manager import DriverManager


class LoginPageObjects:
    def __init__(self):
        self.driver: WebDriver = DriverManager.get_driver()

    def get_agencia_input(self) -> WebElement:
        return self.driver.find_element(By.ID, "bankBranch")

    def get_conta_input(self) -> WebElement:
        return self.driver.find_element(By.ID, "bankAccount")

    def get_avancar_button(self) -> WebElement:
        return self.driver.find_element(By.ID, "submit-login-form")

    def get_senha_button(self, digito: str) -> WebElement:
        return self.driver.find_element(By.XPATH, f"//span[@class='mdc-button__label' and contains(text(), '{digito}')]")

    def get_entrar_button(self) -> WebElement:
        return self.driver.find_element(By.ID, "submit-login-form")
