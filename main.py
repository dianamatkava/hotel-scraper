import json     
from utils.operations import HotelPage


def main():
    
    hotel_page_obj = HotelPage('www.booking.com', 'precise-tale-berlin.en-gb.html')
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
            'alternative_hotels': 'Please checl if booking.com added alternative hotels again'
        }
        return json.dumps(hotel_data, indent=4)


print(main())

