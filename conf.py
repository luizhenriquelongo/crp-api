import os


class Config:
    CFP_URL = 'https://cadastro.cfp.org.br/'
    CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH') or os.path.join(os.path.dirname(__file__), 'chromedriver')
    TIMEOUT = 10
    ELEMENTS_XPATH = {
        'advanced_search_button': '//*[@id="main"]/article/div/div/div[2]/form/div[3]/button[2]',
        'search_button': '//*[@id="main"]/article/div/div/div[2]/form/div[3]/button[1]',
        'name': '//*[@id="main"]/article/div/div/div[2]/div/div/table/tbody/tr/td[2]',
        'region': '//*[@id="main"]/article/div/div/div[2]/div/div/table/tbody/tr/td[3]',
        'register_number': '//*[@id="main"]/article/div/div/div[2]/div/div/table/tbody/tr/td[4]',
        'register_status': '//*[@id="main"]/article/div/div/div[2]/div/div/table/tbody/tr/td[1]',
    }
