from datetime import datetime


def logger(path):
    def wrapper(some_func):
        def my_func(*args):
            date = datetime.now()
            name = my_func.__name__
            items = args
            res = some_func(*args)
            with open(path, 'a') as f:
                f.write(f'date: {date}, function_name: {name}, arguments: {items}, result: {res}')
            return res

        return my_func

    return wrapper
