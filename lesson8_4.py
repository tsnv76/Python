from functools import wraps

def val_checker(flag_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for item in args:
                if flag_func(item):
                    return func(item)
                else:
                    raise ValueError(f'Wrong val  {item}')
        return wrapper
    return _val_checker

@val_checker(lambda x: x>0)
def calc_cube(x):
    return x ** 3

print(calc_cube(-5))
