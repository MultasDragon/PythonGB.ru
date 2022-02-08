# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:44:47 2022

@author: asarlybayev
"""
Stroka = []
b = 0
vveli = True
while vveli:
    Stroka1 = input("Введите своё предложение с пробелами, не мучайте танзанийских хомячков, или просто энтер нажмите: ").split(" ")
    if Stroka1 != ['']:
        Stroka = Stroka + Stroka1
        for i in range(b, len(Stroka)):
            print(f'{i+1:>5}.', Stroka[i][:10])
        b=len(Stroka)
    else:
        vveli = False
print('На этом, не прощаемся с Вами, а говорим лишь до свиданья!')