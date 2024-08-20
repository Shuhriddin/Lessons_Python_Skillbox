# TODO здесь писать код
class Student:

    def __init__(self, full_name, group_number, marks):
        self.full_name = full_name
        self.group_number = group_number
        self.marks = marks


students = [
    Student("Иванов Иван", "Группа-101", [5, 5, 5, 4, 5]),
    Student("Сергев Сергей", "Группа-105", [5, 5, 5, 4, 5]),
    Student("Алеков Алек", "Группа-104", [5, 5, 5, 4, 5]),
    Student("Волков Волк", "Группа-103", [5, 5, 5, 4, 5]),
    Student("Алексеев Влад", "Группа-102", [5, 5, 5, 4, 5]),
    Student("Константин Паоло", "Группа-101", [5, 5, 5, 4, 5]),
    Student("Пашковский Алан", "Группа-102", [5, 5, 5, 4, 5]),
    Student("Василов Станислав", "Группа-103", [5, 5, 5, 4, 5]),
    Student("Андреев Андрей", "Группа-104", [5, 5, 5, 4, 5]),
    Student("Максимов Максим", "Группа-105", [5, 5, 5, 4, 5]),
]


def average_marks(student):
    return sum(student.marks) / len(student.marks)


sorted_students = sorted(students, key=average_marks)

count = 0
for student in sorted_students:
    count += 1
    print(f'{count}. {student.full_name}, {student.group_number}. '
          f'Средный балл: {sum((student.marks)) / len(student.marks)}')