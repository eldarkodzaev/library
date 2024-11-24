from . import messages
from .library import Library
from .extra_inputs import input_year, input_book_id, input_status


def add(library: Library) -> None:
    """Добавляет книгу в библиотеку"""

    book = {
        "title": input("Введите название книги: "),
        "author": input("Введите автора книги: "),
        "year": input_year()
    }

    library.add(book)
    print(messages.BOOK_HAS_BEEN_ADDED)


def delete(library: Library) -> None:
    """Удаляет книгу из библиотеки"""

    if not library.books:
        print(messages.LIBRARY_IS_EMPTY)
        return

    book_id: int = input_book_id()
    try:
        library.delete(book_id)
        print(messages.BOOK_HAS_BEEN_DELETED)
    except IndexError:
        print(messages.BOOK_NOT_FOUND)


def show_all_books(library: Library) -> None:
    """Показывает все книги в библиотеке"""

    books: list[dict] = library.books

    if not books:
        print(messages.LIBRARY_IS_EMPTY)
        return

    for book in books:
        status = "в наличии" if book['status'] == 1 else "выдана"
        print(f"{book['id']}, {book['title']}, {book['author']},",
              f"{book['year']} г., {status}")


def search(library: Library) -> None:
    """Поиск книг по названию, автору или году издания"""

    if not library.books:
        print(messages.LIBRARY_IS_EMPTY)
        return

    query = input("Введите название, автора или год издания книги: ")

    books = library.search(query)
    if not books:
        print(messages.BOOKS_NOT_FOUND)
        return

    print(f"\nНайдено книг ({len(books)} шт):")
    for index, book in enumerate(books, start=1):
        print(f"{index}) {book['title']}, {book['author']}, {book['year']} г.")


def change_status(library: Library) -> None:
    """Изменение статуса книги

    Args:
        library (Library): библиотека
        book_id (int): id книги
        new_status (int): новый статус: 1 - в наличии, 0 - выдана
    """

    if not library.books:
        print(messages.LIBRARY_IS_EMPTY)
        return

    book_id = input_book_id()
    if not library.book_exists(book_id):
        print(messages.BOOK_NOT_FOUND)
        return

    new_status = input_status()

    library.change_status(book_id, new_status)
    print(messages.STATUS_HAS_BEEN_CHANGED)
