"""
Задача 5.2 из курса "Алгоритмы и структуры данных на Phyton":
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
"""
# Исходный скрипт
from collections import defaultdict
from sys import getsizeof
from json import loads, dumps
num_1_16 = input('введите первое шестнадцатеричное число: ')
num_2_16 = input('введите второе шестнадцатеричное число: ')

def list_num(num):
    result = []
    for i in num:
        result.append(i)
    return result

nums = [('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8),
        ('9', 9), ('A', 10), ('B', 11), ('C', 12), ('D', 13), ('E', 14), ('F', 15)]
dict_nums = defaultdict(list)
for k, v in nums:
    dict_nums[k].append(v)

def convert_from_16_to_10(my_list):
    out = 0
    for i in range(len(my_list)):
        res = dict_nums[list(reversed(my_list))[i]][0]
        out += res * 16 ** i
    return out

def convert_from_10_to_16(num, result = ''):
    if num == 0:
        return list(reversed(result))
    else:
        elem = num % 16
        next_num = num // 16
        for k, v in dict_nums.items():
            if v[0] == elem:
                return convert_from_10_to_16(next_num, result=result + k)

list_1_16 = list_num(num_1_16)
list_2_16 = list_num(num_2_16)
num_1_10 = convert_from_16_to_10(list_1_16)
num_2_10 = convert_from_16_to_10(list_2_16)
print(convert_from_10_to_16(num_1_10 + num_2_10))
print(convert_from_10_to_16(num_1_10 * num_2_10))
print(getsizeof(nums))       # 184
print(getsizeof(dict_nums))  # 648

# Оптимизированный вариант

def list_num(num):
    result = []
    for i in num:
        result.append(i)
    return result
# Список nums заменим на кортеж
nums_1 = (('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8),
        ('9', 9), ('A', 10), ('B', 11), ('C', 12), ('D', 13), ('E', 14), ('F', 15))
dict_nums = defaultdict(list)
for k, v in nums_1:
    dict_nums[k].append(v)
# данные для конвертации чисел будем хранить не в defaultdic, а в строке
dumped_dict_nums = dumps(dict_nums)
# удалим ссылки на nums_1 и dict_num, т.к. нам они в дальнейшем больше не понадобятся
del nums_1
del dict_nums
def convert_from_16_to_10(my_list):
    out = 0
    for i in range(len(my_list)):
        res = loads(dumped_dict_nums)[list(reversed(my_list))[i]][0]
        out += res * 16 ** i
    return out

def convert_from_10_to_16(num, result = ''):
    if num == 0:
        return list(reversed(result))
    else:
        elem = num % 16
        next_num = num // 16
        for k, v in loads(dumped_dict_nums).items():
            if v[0] == elem:
                return convert_from_10_to_16(next_num, result=result + k)

list_1_16 = list_num(num_1_16)
list_2_16 = list_num(num_2_16)
num_1_10 = convert_from_16_to_10(list_1_16)
num_2_10 = convert_from_16_to_10(list_2_16)
print(convert_from_10_to_16(num_1_10 + num_2_10))
print(convert_from_10_to_16(num_1_10 * num_2_10))
print(getsizeof(dumped_dict_nums)) # 215
"""
В результате оптимизации скрипта заменили сначала заменил список nums на кортеж, затем заменил словарь dict_nums
, в котором хранились данные по конвертации чисел на json строку и удалили ссылки на не используемые кортеж nums_1
и словарь dict_nums . Получили существенную экономию памяти более чем в три раза.
 """