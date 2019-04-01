# coding: utf-8
import os
import psutil
import sys
print("'Hello world' program started")
print('Hello, World! ')
name = input('Ваше имя: ')
print(name, ', добро пожаловать в мир Python!')
answer = input('Давайте поработаем? (Y/N)')
if answer == 'Y':
    print('''Отлично! Я умею:
    [1] - Выведу список файлов;
    [2] - Выведу информацию о системе
    [3] - Выведу список процессов''')
    do = int(input('Укажите номер действия: '))
    if do == 1:
        print(os.listdir())
    elif do == 2:
        print('Текущая папка: ', os.getcwd())
        print('Платформа(ОС): ', sys.platform)
        print('Имя пользователя: ', os.getlogin())
        print('Количество CPU: ', os.cpu_count())
        print('Кодировка: ', sys.getfilesystemencoding())
    elif do == 3:
        print(psutil.pids())
    else:
        pass
elif answer == 'N':
    print('До свидания!')
else:
    print('Неизвестный выбор')