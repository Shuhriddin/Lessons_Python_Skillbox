# TODO здесь писать код

def count_uppercase_lowercase(text):
    count_upper = 0
    count_lower = 0
    for word in text:
        if word.isupper():
            count_upper += 1
        elif word.islower():
            count_lower += 1
    return count_upper, count_lower

# Пример использования:
text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
