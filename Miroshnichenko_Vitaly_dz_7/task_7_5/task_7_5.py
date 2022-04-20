# Task4
# Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках), размер которых
# не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
#
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import zipfile
import os
import pprint

my_dict = dict()
start_limit = 100


def check_size(size, upper_limit, exp):
    if size <= upper_limit:
        if upper_limit in my_dict:
            my_dict[upper_limit][0] += 1
            if exp not in my_dict[upper_limit][1]:
                my_dict[upper_limit][1].append(exp)
        else:
            my_dict[upper_limit] = [1, [exp]]
    else:
        upper_limit *= 10
        check_size(size, upper_limit, exp)


def search_size_file(path):
    for elem in os.listdir(path):
        cur_path = os.path.join(path, elem)
        if os.path.isdir(cur_path):
            search_size_file(cur_path)
        else:
            file_size = os.path.getsize(cur_path)
            expansion = (os.path.splitext(cur_path)[1])[1:]
            check_size(file_size, start_limit, expansion)


if not os.path.exists('extract dir'):
    os.mkdir('extract dir')

zip_archive = 'some_data.zip'
if zip_archive[:zip_archive.index('.')] not in os.listdir('extract dir'):
    my_zip = zipfile.ZipFile('some_data.zip')
    os.chdir('extract dir')
    my_zip.extractall()
    my_zip.close()
    os.chdir('..')

my_path = os.path.abspath('..')
search_size_file(my_path)

for key, value in my_dict.items():
    my_dict[key] = tuple(value)

pprint.pprint(my_dict)
