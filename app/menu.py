from .actions import add, delete, search, show_all_books, change_status


menu = {
    "1": add,
    "2": delete,
    "3": show_all_books,
    "4": search,
    "5": change_status
}


def print_menu():
    print(
    """
    Выберите действие:
    1) Добавить книгу
    2) Удалить книгу
    3) Показать все книги
    4) Поиск книги
    5) Изменить статус книги
    0) Выход
    """
    )