# coding: utf-8
import os
import psutil
import shutil
import sys


def duplicate_delete(directory):
    file_list = os.listdir(directory)
    counter = 0
    for f in file_list:
        fullname = os.path.join(directory, f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                counter +=1
                print('Файл', fullname, 'был успешно удалён.')
    return counter


def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("Файл ", newfile, " был успешно создан")
            return True
        else:
            print("Возникли проблемы копирования")
            return False


def sys_info():
    print("Вот что я знаю о системе:")
    print("Количество процессоров: ", psutil.cpu_count())
    print("Платформа: ", sys.platform)
    print("Кодировка файловой системы: ", sys.getfilesystemencoding())
    print("Текущая директория: ", os.getcwd())
    print("Текущий пользователь: ", os.getlogin())


def double_files(dirname):
    file_list = os.listdir()
    i = 0
    while i < len(file_list):
        fullname = os.path.join(dirname, file_list[i])
        duplicate_file(fullname)
        i += 1


def main():
    print("'Hello world' program started")
    print('Hello, World! ')
    name = input('Ваше имя: ')
    print(name, ', добро пожаловать в мир Python!')
    answer = ''
    while answer != 'Q':
        answer = input('Давайте поработаем? (Y/N/Q)').upper()
        if answer == 'Y':
            print('''Отлично! Я умею:
            [1] - Выведу список файлов;
            [2] - Выведу информацию о системе
            [3] - Выведу список процессов
            [4] - Продублирую файлы в текущей директории
            [5] - Продублирую указанный Вами файл
            [6] - Удалю все дублированные файлы в указанной директории''')
            do = int(input('Укажите номер действия: '))
            if do == 1:
                print(os.listdir())
            elif do == 2:
                sys_info()

            elif do == 3:
                print(psutil.pids())
            elif do == 4:
                print("Дублирование файлов в текущей директории")
                double_files('.')

            elif do == 5:
                print("Дублирование указанного файла")
                filename = input("Укажите имя файла:")
                duplicate_file(filename)

            elif do == 6:
                print("Удаление дубликатов в директории")
                dirname = input("Укажите имя директории:")
                print('Удалено ', duplicate_delete(dirname), 'файлов')
        elif answer == 'N':
            print("До свидания!")
        else:
            print("Неизвестный ответ")

if __name__ == '__main__':
    main()