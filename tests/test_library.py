import json
import unittest
from copy import copy

from library import Library
from models import Book


class TestLibrary(unittest.TestCase):
    
    test_library_file = "tests/test_library.json"
    
    test_data = [
        {"id": 1, "title": "Book1", "author": "Author1", "year": 2000, "status": 1},
        {"id": 2, "title": "Book2", "author": "Author2", "year": 2001, "status": 0},
        {"id": 3, "title": "Book3", "author": "Author3", "year": 2002, "status": 1}
    ]
    
    def setUp(self):
        with open(self.test_library_file, "w", encoding="utf-8") as json_file:
            json.dump(self.test_data, json_file, indent=2)
        self.library = Library(file="tests/test_library.json")
        
    def test_add(self):
        book = Book(
            title="Book4", author="Author4", year=2003
        )
        self.library.add(book)
        
        with open(self.test_library_file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        
        expected_list = copy(self.test_data)
        expected_list.append(
            {
                "id": 4,
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "status": 1
            }
        )    
        self.assertListEqual(expected_list, data)

    def test_exists(self):
        with self.assertRaises(FileNotFoundError):
            _ = Library(file="tests/test_NOT_EXISTS_library.json")
            
    def test_get_new_id(self):
        self.assertEqual(4, self.library._get_new_id())

    def test_delete(self):
        book_id = 1
        self.library.delete(book_id)
        
        with open(self.test_library_file, "r", encoding="utf-8") as json_file:
            data: list = json.load(json_file)
            
        expected_list = [
            {"id": 2, "title": "Book2", "author": "Author2", "year": 2001, "status": 0},
            {"id": 3, "title": "Book3", "author": "Author3", "year": 2002, "status": 1}
        ]
        self.assertListEqual(expected_list, data)