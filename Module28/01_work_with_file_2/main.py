# TODO здесь писать код
import os.path
class File:
    def __init__(self, filename) -> None:
        """ Инициализирует объект File с указанным именем файла. Аргументы: filename (str): Имя файла. """
        self.filename = filename
        self.file = None

    @property
    def file_exists(self):
        """ Проверяет, существует ли файл по указанному пути. Возвращает:
            bool: True, если файл существует, False в противном случае.
        """
        return os.path.isfile(self.filename)

    def create_file(self):
        """ Создает новый файл, если он еще не существует. """
        if not self.file_exists:
            self.file = open(self.filename, 'w', encoding="UTF-8")

    def __enter__(self):
        """
        Метод, вызываемый при входе в контекст с использованием оператора 'with'.
        Создает файл, если он не существует, и открывает его в режиме добавления.
        Возвращает:
            file: Открытый объект файла.
        """
        self.create_file()
        self.file = open(self.filename, 'a')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Метод, вызываемый при выходе из контекста с использованием оператора 'with'.
        Закрывает файл, если он был открыт.
        Аргументы:
            exc_type: Тип исключения.
            exc_val: Значение исключения.
            exc_tb: Трассировка стека исключения.
        Возвращает:
            bool: True для подавления любых исключений, возникших в контексте.
        """
        if self.file:
            self.file.close()
        return True

with File('AnyText.txt') as my_file:
    my_file.write("SKILLBOX PROJECTS")





