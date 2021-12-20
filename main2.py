# Написать декоратор из п.1, но с параметром – путь к логам.

import os
from datetime import datetime

def param_decorator(target_folder):
    def decorator(func):
        def wrap(*args):
            result = func(*args)
            time = datetime.now().time()
            date = datetime.now().date()

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            with open(target_folder + '/log.txt', 'a') as log:
                log.write(
                    f'date: {date}, time: {time}, function_name: {func.__name__}, result: {result}, args - {args})\n')
            return result
        return wrap
    return decorator


# Та основная функция к которой мы добавляем функционал
@param_decorator('/Users/sergejpetrov/desktop/1')
def create_full_name(name, lastname):
    return name + " " + lastname

print(create_full_name('Sergey', 'Petrov'))