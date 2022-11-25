from abc import ABC, abstractclassmethod
from bs4.element import Tag
from bs4 import BeautifulSoup
import json
from typing import List
import requests
from http.client import responses


class ScraperException:
    status_code: int
    message: str
    
    def __init__(self, status_code, message) -> None:
        self.status_code = status_code
        self.message = message


class ScraperValueException:
    value: str
    
    def __init__(self, value) -> None:
        self.value = value
    
    def get_text(self) -> str:
        return f'{self.value} Not Found'


class HotelRoom:
    room_catigory: str
    
    def __init__(self, room_catigories) -> None:
        self.room_catigories = room_catigories
        
    def __str__(self) -> str:
        return self.room_catigories
    
    
class HotelRoomComposition:
    rooms: List[HotelRoom]        
    
    def __init__(self) -> None:
        self.rooms: List[HotelRoom] = []
    
    def add(self, component: HotelRoom) -> None:
        self.rooms.append(component)

    def remove(self, component: HotelRoom) -> None:
        self.rooms.remove(component)
        component = None
        
        
        
class HotelRating:
    classification: str
    raiting:        int
    
    def __init__(self, classification, raiting) -> None:
        self.classification = classification
        self.raiting = raiting
        
    def __str__(self) -> str:
        return f"{self.classification} {self.raiting}"
    
        
class HotelReview:
    review_name:    str
    review_point:   float
    review_count:   int
    
    def __init__(
        self, review_name, review_point, review_count
    ) -> None:
        self.review_name = review_name
        self.review_point = review_point
        self.review_count = review_count
        
    def __str__(self) -> str:
        return f"{self.review_point} {self.review_name}"
    

class Hotel:
    name:           str
    address:        str
    description:    str
    
    raiting:        HotelRating
    review:         HotelReview
    rooms:          HotelRoomComposition
    
    def __init__(
        self, name, address, description,
    ) -> None:
        self.name = name
        self.address = address
        self.description = description
        
    def __str__(self) -> str:
        return self.name



class AbstractScraper(ABC):
    
    @abstractclassmethod
    def get_general_info(self) -> Hotel:
        ''' Get general info'''
        
    @abstractclassmethod
    def get_rating(self) -> HotelRating:
        ''' Get rating'''
    @abstractclassmethod    
    def get_review_info(self) -> HotelReview:
        ''' Get review info'''
    @abstractclassmethod    
    def get_rooms(self) -> HotelRoomComposition:
        ''' Get description'''


class HotelPage:
    domain:     str
    param:      str
    url:        str
    content:    BeautifulSoup
    scraper:    AbstractScraper
    
    
    def __init__(self, domain, param) -> None:
        self.domain = domain
        self.param = param
        self.url = 'https://' + self.domain
        self.scraper = scraper_conf[self.domain]()
        
    def connect_(self) -> BeautifulSoup | Exception:
        try:
            res = requests.get(
                url=self.url,
                params={
                    scraper_conf[self.domain]['search_param']: self.param
                }
            )
        except Exception as _ex:
            return Exception(_ex)
        finally:
            if res.status_code == 200:
                self.content = BeautifulSoup(res.text, 'lxml')
                return self.content
            else:
                return Exception(responses[res.status_code])
    
    def parse_data(self) -> Hotel | ScraperException:
        (
            hotel, 
            
        ) = self.scraper(self.content)()
        return hotel
        
    def __str__(self) -> str:
        return f'{self.param} {self.param}'

            
# do search, choise resourse
# HotelPage(resourse+search_input)
# validate and give examples
# Define HotelPage scraper
# 
        
class BookingScraper(AbstractScraper):
    body: Tag 
    scraper_status: ScraperException
    
    def __init__(self, content: BeautifulSoup):
        try:
            self.body = content.select_one('.bodyconstraint')
        except Exception as _ex:
            print(_ex)
        finally:
            self.scraper_status = ScraperException(
                status_code=404,
                message="Body Not Found"
            )
        
    def get_general_info(self) -> Hotel:
        
        hotel_name = self.body.find_all(class_='pp-header__title')
        hotel_address = self.body.find_all(class_='hp_address_subtitle')
        hotel_description = self.body.find_all(class_='k2-hp--description')
        
        if not hotel_name:
            hotel_name = [ScraperValueException('Hotel Name')]
        elif not hotel_address:
            hotel_address = [ScraperValueException('Hotel Address')]
        elif not hotel_description:
            hotel_description = [ScraperValueException('Hotel Description')]
        else:
            hotel = Hotel(
                name=hotel_name[0].get_text(),
                address=hotel_address[0].get_text(),
                description=hotel_description[0].get_text()
            )
        return hotel
        
    def get_rating(self) -> HotelRating:
        raiting_block = ''
        ''' Get rating'''
        
    def get_review_info(self) -> HotelReview:
        review_block = ''
        ''' Get review info'''
        
    def get_rooms(self) -> HotelRoomComposition:
        description_block = ''
        ''' Get description'''
        
    # TODO: make calling functions dynamic
    def __call__(self):
        if self.scraper_status.status_code == 404:
            return self.scraper_status
        
        return (
            self.get_general_info(),
            self.get_rating(),
            self.get_review_info(),
            self.get_rooms()
        )
        
        

#   # test case: address should be 1

# ratings = soup.find_all(class_='hp__hotel_ratings__stars')[0]
# if ratings:
#     print(len(ratings.find_all(class_='adc357e4f1')))                   # len shoud not more the max-point
#     print(ratings.find_all(class_='fbb11b26f5')[0]['data-testid'])      # ~~ soulf exist
# review_block = soup.select_one('.b2b990caf1')                                      # only one per page

# review_score = review_block.select_one('.d10a6220b4').get_text()                           # one in for review block
# count_reviews = review_block.select_one('.c90c0a70d3').get_text()



# description = soup.select_one('.k2-hp--description').get_text().replace('\n\n', '\n').replace('\n\n', '\n')




scraper_conf = {
    'booking': {
        'domain': 'booking.com',
        'search_param': 'ss',
        'scraper': BookingScraper
    }
}


booking_conf = {
    'hotel_name': 'pp-header__title',
    'hotel_address': 'hp_address_subtitle',
    'description': 'k2-hp--description',
    
    'rating': {
        'max_rating_points': 5,
        'rating_groups' 'fbb11b26f5 e23c0b1d74'
        'empty_raiting_point': 'b6dc9a9e69 d54be8037c fe621d6382 f86806591e',
        
        
        'point_type': {
            'class': 'fbb11b26f5',
            'identificator': 'data-testid',
            'types': ["rating-stars", "rating-circles", "rating-squares"]
        },
        'point': 'b6dc9a9e69 adc357e4f1 fe621d6382',
        
    },
    'review': {
        'review_block': 'b2b990caf1',
        'revie_score': 'd10a6220b4',
        'count_reviews': 'c90c0a70d3'
    }
}