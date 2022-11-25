# HEADER d2fee87262 
# Address hp_address_subtitle
# hp__hotel_ratings__stars quality-rating rating-stars / rating-circle


#https://www.booking.com/searchresults.en-gb.html?ss=Melia+Berlin 

from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.booking.com/hotel/de/kempinskibristolberlin.en-gb.html'  # check connection
url2 = 'https://www.booking.com/hotel/de/melia-berlin.en-gb.html'
url3 = 'https://www.booking.com/hotel/de/precise-tale-berlin.en-gb.html'

res = requests.get(url)
if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'lxml')
    print(soup.status_code == 404)

# print(soup.find_all(class_='d2fee87262')[0].get_text()) # test case: header should be 1
# print(soup.find_all(class_='hp_address_subtitle')[0].get_text())   # test case: address should be 1

# ratings = soup.find_all(class_='hp__hotel_ratings__stars')[0]
# if ratings:
#     print(len(ratings.find_all(class_='adc357e4f1')))                   # len shoud not more the max-point
#     print(ratings.find_all(class_='fbb11b26f5')[0]['data-testid'])      # ~~ soulf exist
review_block = soup.select_one('.b2b990caf1')                                      # only one per page

review_score = review_block.select_one('.d10a6220b4').get_text()                           # one in for review block
count_reviews = review_block.select_one('.c90c0a70d3').get_text()
count_reviews = review_block.select_one('.c90c0a70d3').get_text()
# print(count_reviews)

description = soup.select_one('.k2-hp--description').get_text().replace('\n\n', '\n').replace('\n\n', '\n')


try:
    count_reviews = review_block.select_one('.c90c0a7e0d3').get_text()
except Exception as _ex:
    print(_ex.obj, _ex.args)
    
# print(count_reviews)

# print(soup.__dir__())


d = {
    'hotel_name': 'd2fee87262',
    'hotel_address': 'hp_address_subtitle',
    
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
    },
    'description': 'k2-hp--description'
    
}
