# Напишите декоратор retry_five, который повторяет вызов декорируемой
# функции 5 раз.

def printstars(iters):
    def actual_decorator(some_func):
        def wrapper(*args, **kwargs):
            for i in range(iters):
                print('*' * 30)
                print(some_func(*args, **kwargs))
                print('*' * 30)
        return wrapper
    return actual_decorator

@printstars(iters=5)
def some_func(some_param):
    result = some_param * 30
    return result

some_func("test")
