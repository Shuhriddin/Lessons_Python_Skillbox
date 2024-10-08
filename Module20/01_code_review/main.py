students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)

# TODO исправить код
def student_info(students):
    student_age_id = [(id, i_student['age']) for id, i_student in students.items()]
    interest = set()
    surname_len = 0
    for student in students.values():
        interest.update(student['interests'])
        surname_len += len(student['surname'])
    return student_age_id, interest, surname_len


age_id, total_interests, len_surname = student_info(students)

print(f'Список пар «ID студента — возраст»: {age_id}')
print(f'Полный список интересов всех студентов: {total_interests}')
print(f'Общая длина всех фамилий студентов: {len_surname}')