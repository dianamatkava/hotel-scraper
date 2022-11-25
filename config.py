from operations import BookingScraper    


scraper_conf = {
    'www.booking.com': {
        'domain': 'booking.com',
        'address_to_hotels': '/hotel/de/',
        'search_param': 'ss',
        'scraper': BookingScraper
    }
}

