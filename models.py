from typing import List

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
    raiting:        int | str
    
    def __init__(self, classification, raiting) -> None:
        self.classification = classification
        self.raiting = raiting
        
    def __str__(self) -> str:
        return f"{self.classification} {self.raiting}"
    
    
        
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
