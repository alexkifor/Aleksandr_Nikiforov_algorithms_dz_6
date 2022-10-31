"""
Задача 4.1 из курса "Алгоритмы и структуры данных на Phyton"
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Попробуйте оптимизировать код, чтобы снизить время выполнения
"""
from numpy import array
from sys import getsizeof

def check_size_arr(func):
    def wrapper(*args):
        func(*args)
        print(getsizeof(func(*args)))
    return wrapper

@ check_size_arr
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# Для сокращения времени был использован lict comprehensions, однако, выделяемую память это не уменьшило

@ check_size_arr
def func_2(nums):
   new_arr = [i for i in range(len(nums)) if i % 2 == 0]
   return new_arr

# Для оптимизации скрипта по памяти используем numpy
@ check_size_arr
def func_3(nums):
    new_arr = array([i for i in range(len(nums)) if i % 2 == 0])
    return new_arr

nums = array([i ** 2 for i in range(10000)])

func_1(nums)  #41880 (Обычный список)
func_2(nums)  #41880 (List comprehensions)
func_3(nums)  #20120 (numpy.ndarray)

"""
Использование array из numpy для хранения результат функции привело к уменьшению выделяемой памяти в два раза
по сравнению с обычным списком.
"""