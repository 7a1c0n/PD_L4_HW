"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

def add_format(time):
    return ' (в формате DD.MM)' * int(time == 'день')

def answer(time):
    return input(f'Введите {time} рождения А.С.Пушкина{add_format(time)}: ')

D_O_B = {'год': '1799', 'день': '06.06'}

for d in D_O_B.keys():
    show_must_go_on = True
    while show_must_go_on:
        if answer(d) == D_O_B[d]:
            print('Верно!')
            show_must_go_on = False
        else:
            print('Неверно')
