from enum import Enum


class Status(Enum):
    """
    Статус книги:
      in_stock - в наличии
      issued - выдана
    """
    in_stock = 1
    issued = 0
    


class Book:
    
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
            
    def to_json(self) -> dict:
        return {
            'id_': self.id_,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }
    