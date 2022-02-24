from time import sleep
from typing import (
    Optional,
    Type,
)

from pydantic import BaseModel
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver import (
    Chrome,
    ChromeOptions,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .config import ScrapperConfig


class CRPUserData(BaseModel):
    name: str
    region: str
    register_number: str
    register_status: str
    is_active: bool = False


class CRPScrapper:
    """TODO update docs Class to validate CRP register.

    This class is used to validate a CRP register using Selenium webdriver
    to validate through CFP website.

    Attributes:
        config: An object with attributes to configure the class, example:
            class Config:
                CFP_URL = https://foobar.com/'

    """

    def __init__(self, config: Type[ScrapperConfig]):
        """Inits CRPValidation with config object"""
        self.config = config()
        self.__driver = self._get_driver()

    def _get_driver(self):
        """Returns a headless selenium webdriver"""
        option = ChromeOptions()
        option.add_argument('headless')
        driver = Chrome(self.config.CHROMEDRIVER_PATH, options=option)
        return driver

    def _get_dom_element(self, element: str) -> WebElement:
        """Gets the DOM element by xpath"""
        return self.__driver.find_element(by=By.XPATH, value=element)

    def scrape_for_user_data(self, register: str, cpf: str) -> Optional[CRPUserData]:
        """Validate the CRP registrer.

        Args:
            register: CRP register number.
            cpf: CPF number.

        Returns:
            (valid_crp, user_data)
        """

        self.__driver.get(self.config.CFP_URL)
        advanced_search_button = self._get_dom_element(self.config.ELEMENTS_XPATH.advanced_search_button)
        search_button = self._get_dom_element(self.config.ELEMENTS_XPATH.search_button)
        register_number_field = self.__driver.find_element(by=By.ID, value='registroconselho')
        cpf_number_field = self.__driver.find_element(by=By.ID, value='cpf')

        advanced_search_button.click()
        sleep(0.5)
        register_number_field.send_keys(register)
        cpf_number_field.send_keys(cpf)
        search_button.click()

        try:
            WebDriverWait(self.__driver, self.config.TIMEOUT).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'resultados'))
            )
            WebDriverWait(self.__driver, self.config.TIMEOUT).until(
                EC.presence_of_element_located(
                    (
                        By.CLASS_NAME, 'table-responsive')
                )
            )

            name = self._get_dom_element(self.config.ELEMENTS_XPATH.name).text
            region = self._get_dom_element(self.config.ELEMENTS_XPATH.region).text
            register_number = self._get_dom_element(self.config.ELEMENTS_XPATH.register_number).text
            register_status = self._get_dom_element(self.config.ELEMENTS_XPATH.register_status).text

            self.__driver.quit()
            return CRPUserData(
                name=name,
                region=region,
                register_number=register_number,
                register_status=register_status,
                is_active=register_status == "ATIVO"
            )

        except (TimeoutException, NoSuchElementException):
            self.__driver.quit()
            return None
