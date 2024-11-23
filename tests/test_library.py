import json
import unittest
from copy import copy

from app.library import Library


class TestLibrary(unittest.TestCase):
    
    test_library_file = "tests/test_library.json"
    
    test_data = [
        {"id": 1, "title": "Book1", "author": "Author1", "year": 2000, "status": 1},
        {"id": 2, "title": "Book2", "author": "Author2", "year": 2001, "status": 0},
        {"id": 3, "title": "Book3", "author": "Author3", "year": 2002, "status": 1},
        {"id": 4, "title": "Book4", "author": "Author1", "year": 2000, "status": 1},
        {"id": 5, "title": "Book4", "author": "Author4", "year": 2000, "status": 0},
        {"id": 6, "title": "1984", "author": "Джордж Оруэлл", "year": 1900, "status": 0},
        {"id": 7, "title": "Book0", "author": "Джордж Оруэлл", "year": 1984, "status": 0},
    ]
    
    def setUp(self):
        with open(self.test_library_file, "w", encoding="utf-8") as json_file:
            json.dump(self.test_data, json_file, indent=2)
        self.library = Library(file="tests/test_library.json")

    def test_get_new_id(self):
        self.assertEqual(8, self.library._get_new_id())
        
    def test_books(self):
        self.assertListEqual(self.test_data, self.library.books)
        
    def test_add(self):
        book = {
            "title": "Book7",
            "author": "Author7",
            "year": 2003
        }
        self.library.add(book)
        
        expected_list = copy(self.test_data)
        expected_list.append(
            {
                "id": 8,
                "title": book['title'],
                "author": book['author'],
                "year": book['year'],
                "status": 1
            }
        )    
        self.assertListEqual(expected_list, self.library.books)

    def test_delete(self):
        book_id = 1
        self.library.delete(book_id)
            
        expected_list = [
            {"id": 2, "title": "Book2", "author": "Author2", "year": 2001, "status": 0},
            {"id": 3, "title": "Book3", "author": "Author3", "year": 2002, "status": 1},
            {"id": 4, "title": "Book4", "author": "Author1", "year": 2000, "status": 1},
            {"id": 5, "title": "Book4", "author": "Author4", "year": 2000, "status": 0},
            {"id": 6, "title": "1984", "author": "Джордж Оруэлл", "year": 1900, "status": 0},
            {"id": 7, "title": "Book0", "author": "Джордж Оруэлл", "year": 1984, "status": 0},
        ]
        self.assertListEqual(expected_list, self.library.books)
        
    def test_search(self):
        # Случай, когда в библиотеке есть только одна книга с таким названием
        query = 'Book1'
        books = self.library.search(query)
        self.assertListEqual(
            [{"id": 1, "title": "Book1", "author": "Author1", "year": 2000, "status": 1}],
            books
        )
        
        # Случай, когда в библиотеке есть несколько книг с одинаковым названием
        query = "Book4"
        books = self.library.search(query)
        expected_list = [
            {"id": 4, "title": "Book4", "author": "Author1", "year": 2000, "status": 1},
            {"id": 5, "title": "Book4", "author": "Author4", "year": 2000, "status": 0},
        ]
        self.assertListEqual(expected_list, books)
        
        # Случай, когда в библиотеке есть несколько книг одного автора
        query = "Author1"
        books = self.library.search(query)
        expected_list = [
            {"id": 1, "title": "Book1", "author": "Author1", "year": 2000, "status": 1},
            {"id": 4, "title": "Book4", "author": "Author1", "year": 2000, "status": 1},
        ]
        self.assertListEqual(expected_list, books)
        
        # Случай, когда в библиотеке есть несколько книг с одной датой выхода
        query = 2000
        books = self.library.search(query)
        expected_list = [
            {"id": 1, "title": "Book1", "author": "Author1", "year": 2000, "status": 1},
            {"id": 4, "title": "Book4", "author": "Author1", "year": 2000, "status": 1},
            {"id": 5, "title": "Book4", "author": "Author4", "year": 2000, "status": 0},
        ]
        self.assertListEqual(expected_list, books)
        
        # Случай, когда в библиотеке есть книги с совпадающими названием и годом издания
        query = "1984"
        books = self.library.search(query)
        expected_list = [
            {"id": 6, "title": "1984", "author": "Джордж Оруэлл", "year": 1900, "status": 0},
            {"id": 7, "title": "Book0", "author": "Джордж Оруэлл", "year": 1984, "status": 0},
        ]
        self.assertListEqual(expected_list, books)

    def test_change_status(self):
        self.library.change_status(book_id=1, new_status=0)
        expected_list = [
            {"id": 1, "title": "Book1", "author": "Author1", "year": 2000, "status": 0},
            {"id": 2, "title": "Book2", "author": "Author2", "year": 2001, "status": 0},
            {"id": 3, "title": "Book3", "author": "Author3", "year": 2002, "status": 1},
            {"id": 4, "title": "Book4", "author": "Author1", "year": 2000, "status": 1},
            {"id": 5, "title": "Book4", "author": "Author4", "year": 2000, "status": 0},
            {"id": 6, "title": "1984", "author": "Джордж Оруэлл", "year": 1900, "status": 0},
            {"id": 7, "title": "Book0", "author": "Джордж Оруэлл", "year": 1984, "status": 0},
        ]
        self.assertListEqual(expected_list, self.library.books)
        

if __name__ == "__main__":
    unittest.main()
