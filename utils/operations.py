import requests
from http.client import responses
from bs4 import BeautifulSoup
from models import Hotel
from config.config import scraper_conf
from utils.exception import ScraperException
from utils.scraper import AbstractScraper


class HotelPage:
    domain:     str
    param:      str
    url:        str
    
    content:    BeautifulSoup
    scraper:    AbstractScraper
    
    def __init__(self, domain, param) -> None:
        self.domain = domain
        self.param = param
        self.url = 'https://' + self.domain + \
            scraper_conf[self.domain]['address_to_hotels'] + param
        self.scraper = scraper_conf[self.domain]['scraper']
        
    def connect_(self) -> BeautifulSoup | Exception:
        try:
            res = requests.get(url=self.url)
        except Exception as _ex:
            res = ScraperException(404, _ex.args)
            return res
        finally:
            if res.status_code == 200:
                self.content = BeautifulSoup(res.text, 'lxml')
                self.content.status_code = 200
                return self.content
            else:
                return ScraperException(
                    res.status_code, responses[res.status_code]
                )
    
    def parse_data(self) -> Hotel | ScraperException:
        scraper = self.scraper(self.content)()
        return scraper
        
    def __str__(self) -> str:
        return f'{self.url}'
