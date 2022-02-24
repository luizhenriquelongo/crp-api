from . import config
from .crp_scrapper import CRPScrapper


def get_scrapper() -> CRPScrapper:
    return CRPScrapper(config=config.ScrapperConfig)
