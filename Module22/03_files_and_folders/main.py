# TODO здесь писать код
import os


def file_sizes(path):
    files_stat = [0, 0, 0]
    for i_elem in os.listdir(path):
        if os.path.isfile(os.path.abspath(os.path.join(path, i_elem))):
            file_path = os.path.abspath(os.path.join(path, i_elem))
            file_size = os.path.getsize(file_path)
            files_stat[0] += file_size
            files_stat[1] += 1
        else:
            files_stat[0] += (file_sizes(os.path.abspath(os.path.join(path, i_elem))))[0]
            files_stat[1] += (file_sizes(os.path.abspath(os.path.join(path, i_elem))))[1]
            files_stat[2] += 1
    return files_stat


path = os.path.abspath(os.path.join('..', '..', 'Module22'))

print('Размер каталога (в Кб):', file_sizes(path)[0] / 1024)
print('Количество файлов:', file_sizes(path)[1])
print('Количество подкаталогов:', file_sizes(path)[2])