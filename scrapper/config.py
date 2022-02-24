import os
from pathlib import Path

from pydantic import BaseModel


class ElementsXPath(BaseModel):
    advanced_search_button: str = '//*[@id="main"]/article/div/div/div[2]/form/div[3]/button[2]'
    search_button: str = '//*[@id="main"]/article/div/div/div[2]/form/div[3]/button[1]'
    name: str = '//*[@id="main"]/article/div/div/div[2]/div/div/table/tbody/tr/td[2]'
    region: str = '//*[@id="main"]/article/div/div/div[2]/div/div/table/tbody/tr/td[3]'
    register_number: str = '//*[@id="main"]/article/div/div/div[2]/div/div/table/tbody/tr/td[4]'
    register_status: str = '//*[@id="main"]/article/div/div/div[2]/div/div/table/tbody/tr/td[1]'


class ScrapperConfig:
    BASE_PATH = BASE_DIR = Path(__file__).resolve().parent.parent
    CFP_URL = 'https://cadastro.cfp.org.br/'
    CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH') or os.path.join(BASE_PATH, 'chromedriver')
    TIMEOUT = 10
    ELEMENTS_XPATH = ElementsXPath()
