# Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.

import os
from datetime import datetime

dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir)

def decorator(func):
    def wrap(*args):
        result = func(*args)
        time = datetime.now().time()
        date = datetime.now().date()
        with open('log.txt', 'a') as log:
            log.write(
                f'date: {date}, time: {time}, function_name: {func.__name__}, result: {result}, args - {args})\n')
        return result
    return wrap


# Та основная функция к которой мы добавляем функционал
@decorator
def create_full_name(name, lastname):
    return name + " " + lastname

print(create_full_name('Sergey', 'Petrov'))