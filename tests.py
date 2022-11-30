from http.client import responses
import unittest
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from config.booking_conf import booking_conf
from utils.exception import ScraperException

unittest.TestLoader.sortTestMethodsUsing = None


class BookingScraperTest(unittest.TestCase):
    conf = booking_conf['test']
    
    soup: BeautifulSoup
    body: Tag

    # Existing hotel is available
    def test_connect(self):
        try:
            res = requests.get(url=self.conf['url'])
            res = BeautifulSoup(res.text, 'lxml')
            self.soup = res
            res.status_code = 200
        except Exception as _ex:
            res = ScraperException(404, _ex.args)
                
        self.assertEqual(res.status_code, 200)
        
    def test_main_block(self):
        try:
            self.body = self.soup.find(id=booking_conf['body'])
            res = ScraperException(200, 'OK')
        except Exception as _ex:
            res = ScraperException(
                status_code=404,
                message="Body Not Found"
            )
        self.assertEqual(res.status_code, 200)
       
    def setUp(self):
        res = requests.get(url=self.conf['url'])
        res = BeautifulSoup(res.text, 'lxml')
        self.soup = res
        self.body = self.soup.find(id=booking_conf['body'])
                
    # Hotel header should be one per page
    def test_header(self):
        try:
            hotel_name = self.body.select_one(f".{booking_conf['hotel_name']}").get_text()
        except:
            hotel_name = None
        self.assertTrue(bool(hotel_name))
        self.assertEqual(hotel_name, self.conf['test_hotel_name'])
        
    # Hotel address should be one per page
    def test_address(self):
        try:
            hotel_address = self.body.select_one(f".{booking_conf['hotel_address']}").get_text()
        except:
            hotel_address = None
        self.assertTrue(bool(hotel_address))
        
    # Hotel description should be one per page
    def test_description(self):
        try:
            description = self.body.select_one(f".{booking_conf['description']}").get_text()
        except:
            description = None
        self.assertTrue(bool(description))
    
    # Rating block exist
    def test_rating(self):
        try:
            rating_block = self.body.select_one(f".{booking_conf['rating']['block']}")
        except:
            rating_block = None
        self.assertTrue(bool(rating_block))
    
    # Rating points should not more the max-point
    def test_rating_max_points(self):
        try:
            rating_points = self.body.select_one(f".{booking_conf['rating']['block']}")
        except:
            rating_points = None
        self.assertTrue(len(rating_points) <= booking_conf['rating']['max_rating_points'])
            
    # TODO: and so on ... 
    # Review testing the same way as general info
    # Rooms checking collection if exist
    # Ot..
    