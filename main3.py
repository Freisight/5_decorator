# Применить написанный логгер к приложению из любого предыдущего д/з.

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

# if __name__ == '__main__':
#     print(create_full_name('Sergey', 'Petrov'))