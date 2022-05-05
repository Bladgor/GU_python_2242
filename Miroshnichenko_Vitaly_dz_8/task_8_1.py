# 1. Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса
# и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re

MY_PATTERN = re.compile(r'^[a-zA-Z\d].+@[a-z]+\.[a-z]+$')
RE_USER = r'^[a-zA-Z\d.]+'
RE_DOMAIN = r'[a-z]+\.[a-z]+$'


def email_parse(mail):
    my_dict = dict()
    result = MY_PATTERN.match(mail)
    try:
        if result:
            user = re.match(RE_USER, mail)
            domain = re.search(RE_DOMAIN, mail)
            my_dict['username'] = user.group()
            my_dict['domain'] = domain.group()
            return my_dict
        else:
            raise ValueError(f'ValueError: wrong email: {mail}')
    except ValueError as exc:
        print(exc)


e_mail = 'someone@geekbrains.ru'
mail_dict = email_parse(e_mail)

if mail_dict:
    print(mail_dict)


e_mail = 'someone@geekbrainsru'
mail_dict = email_parse(e_mail)

if mail_dict:
    print(mail_dict)
