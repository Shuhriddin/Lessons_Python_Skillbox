# TODO здесь писать код
from collections import Counter


def count_unique_characters(unique: str) -> int:
    return sum(list(filter(lambda value: value == 1, Counter(unique.lower()).values())))


# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

if __name__ == '__main__':
    unique_count = count_unique_characters(message)
    print("Количество уникальных символов в строке:", unique_count)
