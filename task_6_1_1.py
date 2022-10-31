"""
Задача 3.1. из курса Основы языка Phyton:
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
num_translate("one")
"один"
"""
from sys import getsizeof


def num_translate(num):
    dict_number = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': "пять",
        'six': 'шесть',
        'seven': 'cемь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    return dict_number.get(num), getsizeof(dict_number)

class NumTranslate:
    __slots__ = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    def __init__(self, zero,one, two, three, four, five, six, seven, eight, nine, ten):
        self.zero = zero
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six
        self.seven = seven
        self.eight = eight
        self.nine = nine
        self.ten = ten

num = NumTranslate('ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять')

print(num_translate('seven'))  #('семь', 640)
print(num.seven)               # семь
print(getsizeof(num))          # 120
"""
Использование слотов в ООП привело к уменьшению количества выделяемой памяти по сранению с обычным словарем 
с 640 до 120 (чуть более 5 раз).
"""
