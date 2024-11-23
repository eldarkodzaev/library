# python 3.10.12
#
# Консольное приложение для управления библиотекой книг. 
# Приложение позволяeт добавлять, удалять, искать и отображать книги. 

import argparse

from app.library import Library
from app.menu import menu, print_menu


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
            print("Неверный ввод. Повторите попытку")
        else:
            menu[keyword](library)


if __name__ == '__main__':
    main()
