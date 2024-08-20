# TODO здесь писать код
class MyDict(dict):
    def get(self, key, default=None):
        return super().get(key, 0)

my_dict = MyDict({"a": 1, "b": 2, "c": 3})
print(my_dict.get("a"))
print(my_dict.get("d"))