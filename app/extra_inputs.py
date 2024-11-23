# Набор специальных функций для ввода различных типов данных
# с обработкой ошибок


def input_year() -> int:
    """Функция для ввода года издания книги.

    Returns:
        int: год издания
    """
    while True:
        try:
            return int(input("Введите год издания: "))
        except ValueError:
            print("Год должен быть целым числом")
            
def input_book_id() -> int:
    """Функция для ввода id книги

    Returns:
        int: id книги
    """
    while True:
        try:
            return int(input("Введите id книги: "))
        except ValueError:
            print("Id должно быть числом")


def input_status() -> int:
    """Функция для ввода статуса книги

    Returns:
        int: статус книги (1 или 0)
    """
    while True:
        try:
            status = int(input("Введите статус (1 - в наличии, 0 - выдана): "))
            if status in (0, 1,):
                return status
            print("Статус должен быть числом (1 или 0)")
        except (ValueError, TypeError):
            print("Статус должен быть числом (1 или 0)")
