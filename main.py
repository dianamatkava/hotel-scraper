import os
import json
import requests
import validators 
from time import sleep
from art import tprint
from bs4 import BeautifulSoup
from config.config import scraper_conf
from utils.operations import HotelPage
from utils.loader import Loader

class bcolors:
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'


def validate_input(user_input:str):
    if len(user_input) > 1:
        if os.path.exists(user_input):
            return True, 'PATH'
        elif validators.url(user_input):
             return True, 'URL'
        else:
            return True, 'NAME'
    return False, None
    

# Just to make it beautiful. 
def beautiful_loading():
    for _ in range(2):
        print()
    with Loader("Loading..."):
        for _ in range(10):
            sleep(0.25)


def get_data():
    pass


# TODO: Search not working
def search_hotel(params: str) -> str:
    conf = scraper_conf[scraper_conf['default']]
    url = f"{conf['search_link']}{params.replace(' ', '+')}"
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'lxml')
        search_res = soup.find_all(class_='d4924c9e74')
        
        print(search_res)
    pass


def main(input_type:str, user_input: str):
    
    if input_type == 'NAME':
        url = search_hotel(user_input)
        hotel_page_obj = HotelPage(
            url=url
        )
        res = hotel_page_obj.connect_()
        
    elif input_type == 'PATH':
        hotel_page_obj = HotelPage(
            path=user_input,
        )
        res = hotel_page_obj.connect_to_file()
    
    elif input_type == 'URL':
        hotel_page_obj = HotelPage(
            url=user_input
        )
        res = hotel_page_obj.connect_()
    
    
    if res.status_code == 200:
        status, hotel = hotel_page_obj.parse_data()
        hotel_data = {
            'hotel_name': hotel.name,
            'hotel_address': hotel.address,
            'description': hotel.description,
            
            'rating': {
                'classification': hotel.raiting.classification,
                'raiting': hotel.raiting.raiting,
            },
            
            'review': {
                'review_name': hotel.review.review_name,
                'review_point': hotel.review.review_point,
                'review_count': hotel.review.review_count
            },
            
            'room': {
                'rooms': [room.r_type for room in hotel.rooms.rooms],
                
            },
            'alternative_hotels': [hotel_name for hotel_name in hotel.other_hotel]
        }
        return json.dumps(hotel_data, indent=4)


if __name__ == '__main__': 
    hotel_name = 'Meliá Berlin'
    hotel_name_ex = hotel_name+' (search for other hotel currently not avialable)'
    hotel_link_ex = 'https://www.booking.com/hotel/de/melia-berlin.en-gb.html'
    hotel_path_ex = 'test_input\Meliá Berlin, Berlin – Updated 2022 Prices.html'
    
    tprint(f'Hotel Scraper CLI', font='bulbhead')
    print(f'''{bcolors.OKCYAN}Input Examples:\n\nHotel Name: {hotel_name_ex}\nHotel Link: {hotel_link_ex}\nHotel Path: {hotel_path_ex}\n\n\nFor now parsing only booking.com{bcolors.ENDC}''')

    # Hendle user input
    validate_status = False
    input_type = None
    user_input = input('Enter Hotel name, url or path to html file: ')
    while not validate_status:
        (
        validate_status,
        input_type
        ) = validate_input(user_input)
        
        if not validate_status:
            print('Input is not valid')
            user_input = input('Enter Hotel name, url or path to html file: ')
        else:
            print(f'Input type: {input_type}')
            if user_input == hotel_name:
                input_type = 'URL'
                user_input = hotel_link_ex
    beautiful_loading()
    
    
    print(main(input_type, user_input))
        

