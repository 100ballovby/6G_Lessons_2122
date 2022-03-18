import random as r
import string as s


def random_keygen(count, length):
    """
    Функция генерирует список случайных паролей
    :param count: количество паролей в списке
    :param length: длина каждого пароля
    :return: список паролей
    """
    passwords = []  # список паролей
    alphabet = s.ascii_letters + s.digits
    # алфавит для паролей - все буквы английского алфавита + цифры
    for i in range(count):
        password = ''  # пароль
        for symbol in range(length):  # повторить length раз
            password += r.choice(alphabet)  # достаю случайный символ из алфавита к паролю
        passwords.append(password)  # добавляю пароль к списку паролей
    return passwords

print(random_keygen(20, 12))


