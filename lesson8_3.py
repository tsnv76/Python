from functools import wraps


def _type_logger(flag_func=0):
    def type_logger(func):
        list_result = []
        @wraps(func)
        def type_wrapper(*args):
            for item in args:
                if flag_func == 0:
                    list_result.append(f'{item}: {type(item)}')
                else:
                    list_result.append(f'{item}: {type(item)}, {func.__name__}')
            return list_result
        return type_wrapper
    return type_logger

@_type_logger(flag_func=0)
def calc_cube(x):
    return x ** 3

print(calc_cube(5, 6, 7, 8))
