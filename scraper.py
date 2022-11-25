import requests
from http.client import responses
from abc import ABC, abstractclassmethod
from bs4 import BeautifulSoup
from bs4.element import Tag
from config import (
    scraper_conf
)
from models import (
    Hotel, HotelRating, HotelReview, 
    HotelRoom, HotelRoomComposition
)
from exception import (
    ScraperException, ScraperValueException
)
from operations import AbstractScraper

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

        

        
# do search, choise resourse
# HotelPage(resourse+search_input)
# validate and give examples
# Define HotelPage scraper
# 
                
def test():
    url = 'https://www.booking.com/hotel/de/kempinskibristolberlin.en-gb.html'  # check connection
    url2 = 'https://www.booking.com/hotel/de/melia-berlin.en-gb.html'
    url3 = 'https://www.booking.com/hotel/de/precise-tale-berlin.en-gb.html'
    
    hotel_page_obj = HotelPage('www.booking.com', 'precise-tale-berlin.en-gb.html')
    hotel_html = hotel_page_obj.connect_()
    if hotel_html.status_code == 200:
        status, hotel = hotel_page_obj.parse_data()
        print(status.status_code)
        print(hotel.name, hotel.address,
              hotel.raiting.raiting, hotel.raiting.classification, 
               hotel.review.review_count, hotel.review.review_point, hotel.review.review_name, sep='\n')
    
test()







