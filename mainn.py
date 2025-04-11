import os
import datetime
import logging
from functools import wraps




def logger(old_function):

    @wraps(old_function)
    def new_function(*args, **kwargs):
        logging.basicConfig(filename='mainn.log', level=logging.INFO, encoding='utf-8')
        func_call_time = datetime.datetime.now()
        result = old_function(*args, **kwargs)

        logging.info(f'Дата и время вызова функции: {func_call_time}.')
        logging.info(f'Название функции: {old_function.__name__}.')
        logging.info(f'Позиционные аргументы: {args}, именованные: {kwargs}.')
        logging.info(f'Возвращаемое значение: {result}.')
        logging.info('')

        return result

    return new_function


def mainn():
    path = 'mainn.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World, I study in Netology 20.10.2024'

   
    assert 'Hello World, I study in Netology 20.10.2024' == hello_world(), "Функция возвращает 'Hello World, I study in Netology 20.10.2024'"
   

    assert os.path.exists(path), 'файл mainn.log должен существовать'

   

    with open(path) as log_file:
        log_file_content = log_file.read()

   


if __name__ == '__main__':
    mainn()
        