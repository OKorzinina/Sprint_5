from random import randint

class Person:
    user_name = 'Olga'
    email = f'korzininao@gmail.com'
    password = f'12345Kor@'

class RandomData:
    user_name = 'Тест'
    email = f'test{randint(0, 999)}@gmail.com'
    password = f'{randint(1000, 9999)}Kor@'
