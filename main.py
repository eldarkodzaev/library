# python 3.10.12

import argparse
import sys

from models import Book
from library import Library


def add(library: Library):
    """Добавляет книгу в библиотеку"""
    
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = int(input("Введите год издания: "))

    book = Book(title, author, year)
    library.add(book)
    print("Книга добавлена в библиотеку")


def delete(library: Library):
    """Удаляет книгу из библиотеки"""
    
    book_id = int(input("Введите id книги: "))
    try:
        library.delete(book_id)
        print("Книга удалена из библиотеки")
    except ValueError as e:
        print(e)

 
def show_all(library: Library):
    """Показывает все книги в библиотеке"""

    if (books := library.books):
        for book in books:
            print(f"{book['id']}, {book['title']}, {book['author']}, {book['year']}, {book['status']}")
    else:
        print("В библиотеке пока нет никаких книг")
        

def search(library: Library):
    """Поиск книг"""
    
    query = input("Введите запрос для поиска: ")
    
    books = library.search(query)
    if not books:
        print("По введенному запросу не найдено ни одной книги")
    else:
        print(f"\nНайдено {len(books)} книг:")
        for index, book in enumerate(books, start=1):
            print(f"{index}) {book['title']}, {book['author']}, {book['year']}")
    
        

def print_menu():
    print(
    """
    Выберите действие:
    1) Добавить книгу
    2) Удалить книгу
    3) Показать все книги
    4) Поиск книги
    0) Выход
    """
    )

    
menu = {
    "1": add,
    "2": delete,
    "3": show_all,
    "4": search
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Библиотека")
    parser.add_argument("library", type=str, help="Путь к файлу библиотеки")
    args = parser.parse_args()
    
    library = Library(args.library)
    
    keyword = None

    while True:
        print_menu()
        keyword = input(">>> ")
        
        if keyword == "0":
            print("Программа завершена")
            return
        
        if keyword not in menu:
            print("Неверный ввод. Повторите попытку", file=sys.stderr)
        else:
            menu[keyword](library)


if __name__ == '__main__':
    main()
