# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 19:06:18 2022
@author: asarlybayev
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def checint(x):#проверка на целочисленность, если не целочисленное - то 0,
    if type(x) is int:
        return x
    if type(x) is str:
        if x.replace(" ","").replace("-","").isnumeric():
            return int(x.replace(" ",""))
        else:
            print(f'{x} - не целое число')
            return 0

def checfloat(x):#проверка на дробночисленность, если не дробночисленное - то 0,
    if type(x) is float:
        return x
    if type(x) is int:
        return float(x)
    if type(x) is str:
        x = x.replace(" ","").replace(",",".")
        if x.replace(".","").replace("-","").isnumeric():
            if x[0] == ".":
                x = '0' + x
            return float(x)
        else:
            print(f'{x} - не число')
            return 0.0

def de2ch(x1, x2):
    x1, x2 = checfloat(x1), checfloat(x2)

    if x2 == 0.0:
        print('Деление на ноль, по техническим причинам, на сегодня не предоставляется, за разъяснениями к математикам')
    else:
        print(f'{x1} делить на {x2} равно {x1/x2:.5f}')        

de2ch(112," ,a")
de2ch(112," ,1")
de2ch(112,"- ,1")
de2ch(112,"-0,1")
de2ch(input('Введите делимое: '), input('Введите делитель: '))
print(f'И не забудьте похлопать в ладоши!') 

""" и второй вариант:
    """
    
def check_delim(x1, x2):
    if x1 == "" or x2 == "":
        return ""
    try:
        return f"{x1} / {x2} = {x1/x2}"
    except:
        return "Деление невозможно, нуль-с"
def check_val(x):
    try:
        return float(x)
    except:
        return check_val(input("Ну позязя "))

print(check_delim(check_val(input('Введите делимое: ')),check_val(input('Введите делитель: '))))

#а так и вправду короче, надо подучить