# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
#
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)


def type_logger(func):

    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        all_args = []
        for i_arg in args:
            all_args.append(i_arg)
        for i_kwarg in kwargs.values():
            all_args.append(i_kwarg)
        print(f'{func.__name__}(', end='')
        for i, elem in enumerate(all_args):
            if i + 1 != len(all_args):
                print(f'{elem}: {type(elem)}', end=', ')
            else:
                print(f'{elem}: {type(elem)})')
        return result
    return wrapped


@type_logger
def calc_cube(*args, x=None):
    arguments = args
    my_list = []
    for elem in arguments:
        my_list.append(elem ** 3)
    my_list.append(x ** 3)
    return my_list


a = calc_cube(5, 6, 7.5, x=4)
print(a)
