"""
Задача 5.5 из курса Основы Phyton:
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке.
"""
from sys import getsizeof
from time import perf_counter
# решение через list comprehensions

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start = perf_counter()
result = [num for num in src if src.count(num) == 1]
end = perf_counter()
print(result, getsizeof(result), f'{end - start} сек.')

# оптимизируем решение через filter

optim_res = filter(lambda x: src.count(x) == 1, src)
print(list(optim_res), getsizeof(optim_res))

"""
Использование filter позволило уменьшить выделяему память более чем в 2 раза с 120 до 48
"""