# TODO здесь писать код
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = OrderedDict()

    @property
    def cache(self):
        key, value = next(iter(self.cache_dict.items()))
        return key, value

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self.cache_dict:
            del self.cache_dict[key]
        elif len(self.cache_dict) >= self.capacity:
            self.cache_dict.popitem(last=False)
        self.cache_dict[key] = value

    def get(self, key):
        if key in self.cache_dict:
            value = self.cache_dict[key]
            del self.cache_dict[key]
            self.cache_dict[key] = value
            return value
        return None

    def print_cache(self):
        print("LRU Cache:")
        for key, value in self.cache_dict.items():
            print(f"{key} : {value}")

# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4