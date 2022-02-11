# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:20:40 2022

@author: asarlybayev
2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: 
    имя, 
    фамилия, 
    год рождения, 
    город проживания, 
    email, 
    телефон. 
Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.
"""


import sys

def polcovatel(Imya, Familiya, GodRozhdeniya, GorodProzhivaniya, Email, Nofelet):
    print(f'Товарищи, {Imya} {Familiya} зарегистрировали факт рождения в {GodRozhdeniya} году в великом граде {GorodProzhivaniya}. Контакты: {Email}; {Nofelet}')

def stringami(liter, at = False):
    while liter == "":
        liter = input('Ну позяяяяяяязя ')
        if liter.upper() == "Q":
                return "Q"
    while at and not("@" in liter and (liter[-3] == "." or liter[-4] == "." or liter[-2] == ".") and len(liter) > 4):
        liter = input('Ну позяяяяяяязя ')
        if liter.upper() == "Q":
            return "Q"
    return liter

def inter(val, God):
    while val == "Q":
        return "Q"
    if God:
        while not(('+' in val and val[1:].isdigit()) or val.isdigit()):
            val = input('Ну позяяяяяяязя ')
            if val.upper() == "Q":
                return "Q"
    else:
        while len(val) > 4 and not(val.isdigit()):
            val = input('Ну позяяяяяяязя ')
            if val.upper() == "Q":
                return "Q"
    return val
print('Давайте договоримся, как только вы ввели "Q" - мы прерываемся, ок?')
while True:
    luc1 = stringami(input('Гражданочка, а не подскажете, как вас зовут (stringami)? ').title())
    if luc1.upper() == "Q":
        break
    luc2 = stringami(input('А родовое имя (stringami)? ').title())
    if luc2.upper() == "Q":
        break
    luc3 = inter(input('То есть появились на свет Вы в году (intom не длиннее 4х цифр, так как говорим в 2022ом году) '), False)
    if not(luc3.isdigit()):
        if luc3.upper() == "Q":
            break
    luc4 = stringami(input('А город (stringami)? ').title())
    if luc4.upper() == "Q":
        break
    luc5 = stringami(input('А если я захочу послать Вам весточку елестронной почтой (stringami с @ литералом и завершение на дот две буквы)? '), at = True)
    if luc5.upper() == "Q":
        break
    luc6 = inter(input('Ну а телефончик - чисто, чтобы сообщить когда ставить чайник (токмо цифирью, ну максимум "+"): '), True)
    if not(luc6.isdigit):
        if luc6.upper() == "Q":
            break
    polcovatel(
            Imya = luc1,
            Familiya = luc2,
            GodRozhdeniya = luc3,
            GorodProzhivaniya = luc4,
            Email = luc5,
            Nofelet = luc6
            )
