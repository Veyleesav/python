# coding: utf-8
print("'Hello world' program started")
print('Hello, World! ')
name = input('Ваше имя: ')
print(name, ', добро пожаловать в мир Python!')
answer = input('Давайте поработаем? (Y/N)')
if answer == 'Y':
    print('''Чем бы вы хотели заняться?
    А - Грокать алгоритмы
    В - Анализировать данные
    С - подбирать коэффициенты, пока кросс-валидация не даст нормальный результат''')
elif answer == 'N':
    print('До свидания!')
else:
    print('Неизвестный выбор')