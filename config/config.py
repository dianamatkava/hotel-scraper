from utils.scraper import BookingScraper    


scraper_conf = {
    'default': 'www.booking.com',
    'www.booking.com': {
        'domain': 'booking.com',
        'address_to_hotels': '/hotel/de/',
        'search_param': 'ss',
        'search_result_class': 'a4225678b2',
        'search_link': 'https://www.booking.com/searchresults.en-gb.html?&ss=',
        'scraper': BookingScraper
    }
}

