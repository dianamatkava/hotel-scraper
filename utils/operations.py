import requests
from http.client import responses
from bs4 import BeautifulSoup
from models import Hotel
from config.config import scraper_conf
from utils.exception import ScraperException
from utils.scraper import AbstractScraper


class HotelPage:
    domain:     str
    param:      str | None
    url:        str | None
    path:       str | None
    
    content:    BeautifulSoup
    scraper:    AbstractScraper
    
    def __init__(
        self, domain:str=None, url:str=None, path:str=None
    ) -> None:
        if path:
            self.path = path
            self.scraper = scraper_conf[scraper_conf['default']]['scraper']
        elif url:
            self.domain = scraper_conf['default']
            self.url = url
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
    
    def connect_to_file(self) -> BeautifulSoup | Exception:
        with open(self.path, encoding="utf8") as file:
            self.content = BeautifulSoup(file, 'lxml')
            if self.content:
                self.content.status_code = 200
                return self.content
        return ScraperException(404, "File or Content not found")
        
    def parse_data(self) -> Hotel | ScraperException:
        scraper = self.scraper(self.content)()
        return scraper
        
    def __str__(self) -> str:
        return f'{self.url}'
