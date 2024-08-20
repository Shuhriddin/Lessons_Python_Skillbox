# TODO здесь писать код

def is_palindrome(num_list):
    revese_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        revese_list.append(num_list[i_num])
    if num_list == revese_list:
        return True
    else:
        return False

count_number = int(input('Количество чисел: '))
count = 0
num_list = []
for i in range(count_number):
    number = int(input('Число: '))
    num_list.append(number)


new_nums = []
answer = []

for i_nums in range(0, len(num_list)):
    for j_elem in range(i_nums, len(num_list)):
        new_nums.append(num_list[j_elem])
    if is_palindrome(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(num_list[i_answer])
        answer.reverse()
        break
    new_nums = []

print(f'Последовательность: {num_list}')
print('Нужно приписать чисел:', len(answer))
print('Сами числа:', answer)



