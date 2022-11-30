from typing import List

class HotelRoom:
    r_type:         str
    
    def __init__(self, r_type) -> None:
        self.r_type = r_type
        
    def __str__(self) -> str:
        return self.r_type
    
    
class HotelRoomComposition:
    rooms: List[HotelRoom]        
    
    def __init__(self) -> None:
        self.rooms: List[HotelRoom] = []
    
    def add(self, component: HotelRoom) -> None:
        self.rooms.append(component)
        
    # bulk create
    def extend(self, component: HotelRoom) -> None:
        self.rooms.extend(component)

    def remove(self, component: HotelRoom) -> None:
        self.rooms.remove(component)
        component = None
    
    def __repr__(self) -> str:
        return f'{[room.r_type for room in self.rooms]}'
        
        
class HotelRating:
    classification: str
    rating:        int | str
    
    def __init__(self, classification, rating) -> None:
        self.classification = classification
        self.rating = rating
        
    def __str__(self) -> str:
        return f"{self.classification} {self.rating}"
    
        
class HotelReview:
    review_name:    str
    review_point:   str
    review_count:   str
    
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
    
    rating:        HotelRating 
    review:         HotelReview
    rooms:          HotelRoomComposition
    other_hotel:    List[str]#List[Hotel]
    
    def __init__(
        self, name, address, description,
    ) -> None:
        self.name = name.replace('\n', '')
        self.address = address.replace('\n', '')
        self.description = description.replace('\n\n', '\n').replace('\n\n', '\n')
        self.other_hotel = []
        
     # bulk create
    def add_other_hotel(self, hotel: str) -> None:
        self.other_hotel.append(hotel)
        
    def __str__(self) -> str:
        return self.name
