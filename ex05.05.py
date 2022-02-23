# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 23:35:04 2022

@author: asarlybayev
"""
from random import random

recreate = input("Введите целое число - сколькими чиселками заполонить файло: ")
while not(recreate.isnumeric()):
    recreate = input('Ну позязя, если введешь "Q" - выйдешь из программы: ')
    if recreate.upper() == "Q":
        break
if recreate.isnumeric():
    recreate = int(recreate)
    with open("HoakinPhoenix_num.txt", 'w+', encoding = "utf-8") as FIFO:
        k = [random()*100 for i in range(recreate)]
        print(*k, file = FIFO)
        FIFO.seek(0)
        k = FIFO.readline().split(" ")
        summa = 0
        for i in k:
            summa += float(i)
        print(f'всего в файле {FIFO.name} - {summa}')