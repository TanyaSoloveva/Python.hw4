#2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — 
# значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.


def return_kwargs(**kwargs):
    tmp_dict = {}

    for key, value in kwargs.items():
        try:
            hash(key)
            tmp_dict[value] = key
        except TypeError:
            tmp_dict[str(value)] = key

    return tmp_dict


if __name__ == '__main__':
    try:
        print(return_kwargs(a=[2, 6, 3], b=51))
    except TypeError:
        print('Ошибка')