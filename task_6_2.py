from memory_profiler import profile
@profile()
def func():
    def reversed_num(num, result=''):
        if num == 0:
            print(result)
        else:
            return reversed_num(num//10, result + str(num % 10))

func()
"""
В случае прямого профилирования рекурсии мы получим многократный вызов profile, чтобы этого избежать нужно рекурсию
нужно обернуть в другую функцию и сделать профилирование этой функции.
"""
