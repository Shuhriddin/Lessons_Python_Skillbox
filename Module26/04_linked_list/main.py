# TODO здесь писать код
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return f"[{self.data}]->{self.next}"

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def get(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError('Индекс вне диапазона')
            current = current.next
        if current is None:
            raise IndexError('Индекс вне диапазона')
        return current.data
    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(index - 1):
            if current is None:
                raise IndexError('Индекс вне диапазона')
            current = current.next
        if current is None or current.next is None:
            raise IndexError('Индекс вне диапазона')
        current.next = current.next.next

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return '[' + ' '.join(elements) + ']'

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
