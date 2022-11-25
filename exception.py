
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

