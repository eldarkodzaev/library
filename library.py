import json
import os
from typing import List
from json.decoder import JSONDecodeError

from models import Book


class Library:
    
    def __init__(self, file: str) -> None:
        self.file = file
        if not self._exists():
            with open(file, "w", encoding="utf-8"):
                print(f"(i) Создана новая библиотека {file}")
        else:
            print(f"(i) Подключено к библиотеке {file}")
    
    @property
    def books(self) -> list[dict]:
        """Возвращает список книг

        Returns:
            list[dict]: список словарей
        """
        with open(self.file, "r", encoding="utf-8") as json_file:
            try:
                library: list = json.load(json_file)
                return library
            except JSONDecodeError:
                return []

    def add(self, book: Book) -> None:
        """Добавляет книгу в библиотеку

        Args:
            book (Book): книга
        """
        new_id = self._get_new_id()
        
        library: list = []
        with open(self.file, "r", encoding="utf-8") as json_file:
            try:
                library = json.load(json_file)
            except JSONDecodeError:
                print("Неверный формат JSON-файла")
        
        library.append(
            {
                "id": new_id,
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "status": 1
            }
        )
        
        with open(self.file, "w", encoding="utf-8") as json_file:
            json.dump(library, json_file, ensure_ascii=False)
        
    def delete(self, book_id: int) -> None:
        """Удаляет книгу из библиотеки

        Args:
            book_id (int): id книги
        """
        
        with open(self.file, "r", encoding="utf-8") as json_file:
            data: list = json.load(json_file)
        
        book_for_delete = None  
        for book in data:
            if book['id'] == book_id:
                book_for_delete = book
                break
        
        if book_for_delete:
            data.remove(book_for_delete)
            with open(self.file, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, ensure_ascii=False)
        else:
            raise ValueError(f"Книги с id {book_id} нет в библиотеке")
        
    def search(self, query: str) -> List[Book]:
        """Поиск книг по названию, автору или году

        Args:
            query (str): строка для поиска

        Returns:
            List[Book]: список книг
        """
        with open(self.file, "r", encoding="utf-8") as json_file:
            library: list = json.load(json_file)
        
        books: list = []
        for book in library:
            if (query == book['title'] or
                query == book['author'] or
                query == book['year']):
                books.append(book)
        
        return books
    
    def set_status(self, book_id: int, new_status: int):
        """Задает новый статус книги

        Args:
            book_id (int): id книги
            new_status (int): 1 - в наличии, 0 - выдана
        """
        
    def _exists(self) -> bool:
        """Проверяет, существует ли файл базы данных"""
        
        return os.path.isfile(self.file)
    
    def _get_new_id(self) -> int:
        """Возвращает новый уникальный id"""
        
        data = []
        with open(self.file, "r", encoding="utf-8") as json_file:
            try:
                data: list = json.load(json_file)
            except JSONDecodeError:
                print("Неверный формат JSON-файла")

        ids = [item['id'] for item in data]
        if ids:
            return max(ids) + 1
        return 1
