"""
Задача 7.4 из курса Основы Phyton:
Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0)
"""

import os
from sys import getsizeof
from collections import namedtuple

def stat():
    folder = 'some data'
    path = r'C:\Users\User\PycharmProjects\dz_7'
    folder_path = os.path.join(path, folder)
    size_100000 = []
    size_10000 = []
    size_1000 = []
    size_100 = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if os.stat(os.path.join(root, file)).st_size > 10000:
                size_100000.append(file)
            elif os.stat(os.path.join(root, file)).st_size < 10000:
                size_10000.append(file)
            elif os.stat(os.path.join(root, file)).st_size < 1000:
                size_1000.append(file)
            elif os.stat(os.path.join(root, file)).st_size < 100:
                size_100.append(file)
    result = {100000: len(size_100000), 10000: len(size_10000), 1000: len(size_1000), 100: len(size_100)}
    return result

print(getsizeof(stat())) #232

# Оптимизируем функцию, используя namedtuple

def tuple_stat():
    folder = 'some data'
    path = r'C:\Users\User\PycharmProjects\dz_7'
    folder_path = os.path.join(path, folder)
    size_100000 = []
    size_10000 = []
    size_1000 = []
    size_100 = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if os.stat(os.path.join(root, file)).st_size > 10000:
                size_100000.append(file)
            elif os.stat(os.path.join(root, file)).st_size < 10000:
                size_10000.append(file)
            elif os.stat(os.path.join(root, file)).st_size < 1000:
                size_1000.append(file)
            elif os.stat(os.path.join(root, file)).st_size < 100:
                size_100.append(file)
    out = namedtuple('stat_', ('k100', 'k10', 'k1', 'k01k'))
    res = out(k100=len(size_100000), k10=len(size_10000), k1=len(size_1000), k01k=len(size_100))
    return res

print(getsizeof(tuple_stat())) #72

"""В результате применения namedtuple получили экономию по памяти более чем в 3 раза."""