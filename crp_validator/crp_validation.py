from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .config_object_helper import ConfigObjectHelper as coh


class CRPValidation:
    """Class to validate CRP register.

    This class is used to validate a CRP register using Selenium webdriver
    to validate through CFP website.

    Attributes:
        config: An object with attributes to configure the class, example:
            class Config:
                CFP_URL = https://foobar.com/'

    """
     
    REQUIRED_ATTRIBUTES = ['CFP_URL', 'ELEMENTS_XPATH', 'CHROMEDRIVER_PATH']
    
    def __init__(self, config: object):
        """Inits CRPValidation with config object"""
        self._set_config_attributes(config)
        self.__driver = self._get_driver()
        self.is_valid = False

    def _set_config_attributes(self, config: object):
        """Gets all attributes (not methods) inside the config object and
        convert to attributes in CRPValidation class"""
        if coh.has_required_attributes(self.REQUIRED_ATTRIBUTES):
            attributes = [attr for attr in dir(config) if coh.valid_attibute(
                attr, config)]
    
            for attribute in attributes:
                setattr(self, attribute, eval(f'config.{attribute}'))
    
    def _get_driver(self):
        """Returns a headless selenium webdriver"""
        option = ChromeOptions()
        option.add_argument('headless')
        driver = Chrome(self.CHROMEDRIVER_PATH, options=option)
        return driver

    def _get_dom_element(self, element: str):
        """Gets the DOM element if the xpath is properly defined on config"""
        if element not in self.ELEMENTS_XPATH:
            raise KeyError(f"{element} xpath not found in Config")
        return self.__driver.find_element_by_xpath(
            self.ELEMENTS_XPATH[element])
    
    def _get_user_data(self):
        """Gets all user data within the results after checking the CRP"""
        user_data = {
            'name': self._get_dom_element('name').text,
            'region': self._get_dom_element('region').text,
            'register_number': self._get_dom_element('register_number').text,
            'register_status': self._get_dom_element('register_status').text,
        }

        return user_data

    def validate_crp_register(self, register: str, cpf: str):
        """Validate the CRP registrer.
    
        Args:
            register: CRP register number.
            cpf: CPF number.
    
        Returns:
            Boolean
        """

        self.__driver.get(self.CFP_URL)
        advanced_search_button = self._get_dom_element(
            'advanced_search_button')
        search_button = self._get_dom_element('search_button')
        register_number_field = self.__driver.find_element_by_id(
            'registroconselho')
        cpf_number_field = self.__driver.find_element_by_id('cpf')
    
        advanced_search_button.click()
        sleep(0.5)
        register_number_field.send_keys(register)
        cpf_number_field.send_keys(cpf)
        search_button.click()

        try:
            WebDriverWait(self.__driver, self.TIMEOUT).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'resultados')))
            WebDriverWait(self.__driver, self.TIMEOUT).until(
                EC.presence_of_element_located((
                    By.CLASS_NAME, 'table-responsive')))

            user_data = self._get_user_data()

        except (TimeoutException, NoSuchElementException):
            user_data = {}

        else:
            if user_data['register_status'] == "Ativo":
                self.is_valid = True

        finally:
            self.__driver.quit()
            return self.is_valid, user_data
