import json
import os
from json.decoder import JSONDecodeError

from . import messages


class Library:
    """
    Класс 'Библиотека'.
    Работает непосредственно с базой данных (JSON-файлом)
    """
    
    def __init__(self, file: str) -> None:
        self.file = file
        if not self._library_exists():
            with open(file, "w", encoding="utf-8"):
                print(f"(i) Создана новая библиотека '{file}'")
        else:
            print(f"(i) Подключено к библиотеке '{file}'")
    
    @property
    def books(self) -> list[dict]:
        """Возвращает список книг в библиотеке

        Returns:
            list[dict]: список словарей всех книг в библиотеке:
            [
                {"id": 1, "title": "Book1", "author": "Author1", "year": 2001, "status": 1},
                {"id": 2, "title": "Book2", "author": "Author2", "year": 2002, "status": 0},
                {"id": 3, "title": "Book3", "author": "Author3", "year": 2003, "status": 1},
            ]
        """
        
        with open(self.file, "r", encoding="utf-8") as json_file:
            try:
                return json.load(json_file)
            except JSONDecodeError:
                # Если JSON-структура нарушена, то файл будет перезаписан
                return []

    def add(self, book: dict) -> None:
        """Добавляет книгу в библиотеку

        Args:
            book (dict): книга
        """

        books: list[dict] = self.books        
        books.append(
            {
                "id": self._get_new_id(),
                "title": book['title'],
                "author": book['author'],
                "year": book['year'],
                "status": 1
            }
        )
        
        self._rewrite_library(new_data=books)
        
    def delete(self, book_id: int) -> None:
        """Удаляет книгу из библиотеки

        Args:
            book_id (int): id книги
        """
        
        if not self.book_exists(book_id):
            raise IndexError(messages.BOOK_NOT_FOUND)
        
        books = self.books
        book_for_delete = None
         
        for book in books:
            if book['id'] == book_id:
                book_for_delete = book
                break
        
        books.remove(book_for_delete)
        self._rewrite_library(new_data=books)
        
    def search(self, query: str) -> list[dict]:
        """Поиск книг по названию, автору или году

        Args:
            query (str): строка для поиска

        Returns:
            List[Book]: список книг
        """
        
        founded_books: list[dict] = []
        for book in self.books:
            if (query == book['title'] or
                query == book['author'] or
                query == book['year'] or
                query == str(book['year'])):
                founded_books.append(book)
        
        return founded_books
    
    def change_status(self, book_id: int, new_status: int) -> None:
        """Задает новый статус книги

        Args:
            book_id (int): id книги
            new_status (int): 1 - в наличии, 0 - выдана
        """
        if new_status not in (0, 1,):
            raise ValueError("Статус должен быть либо 1 либо 0")
        
        books: list[dict] = self.books
        for book in books:
            if book['id'] == book_id:
                book['status'] = new_status
                break
            
        self._rewrite_library(new_data=books)

    def book_exists(self, book_id: int) -> bool:
        """Проверяет, существует ли книга с указанным id

        Args:
            book_id (int): id книги

        Returns:
            bool: True/False
        """
        return any([book['id'] == book_id for book in self.books])
        
    def _library_exists(self) -> bool:
        """Проверяет, существует ли файл базы данных"""
        
        return os.path.isfile(self.file)
        
    def _get_new_id(self) -> int:
        """Возвращает новый уникальный id"""

        return max([book['id'] for book in self.books], default=0) + 1
    
    def _rewrite_library(self, new_data: list[dict]) -> None:
        """Перезаписывает библиотеку с новыми данными

        Args:
            new_data (_type_): новые данные
        """
        
        with open(self.file, "w", encoding="utf-8") as json_file:
            json.dump(new_data, json_file, ensure_ascii=False)
