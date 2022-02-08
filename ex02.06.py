# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:31:02 2022

@author: asarlybayev
""" #Я верю в благоразумие ваше и мне лень делать проверку на вшивость ввода, посему не делал :(

MY_list = []
#MY_list = [(1, {'Название': 'Компьютер', 'Цена': 20000.0, 'Количество': 5, 'ед': 'ед.'}), (2, {'Название': 'Принтер', 'Цена': 6000.0, 'Количество': 2, 'ед': 'ед'}), (3, {'Название': 'Сканер', 'Цена': 2000.0, 'Количество': 7, 'ед': 'ед'})]
iCounter = 1
while True:
    Name_good = input('Введите название товара: ')
    if Name_good == "":
        break
    Price = float(input('Введите цену за товар: '))
    if Price == 0:
        break
    Size = input('Введите единицу размерности товара: ')
    if Size == "":
        break
    Qty = int(input('Введите количество товара в единицах размерности: '))
    if Qty == "":
        break
    MY_list.append((iCounter, {"Название": Name_good, "Цена": Price, "Количество": Qty, "ед": Size}))
    iCounter += 1

#print(MY_list)

listik={}
for i in MY_list:    
    for j in i[1]:
        listik[j] = 0
listik = tuple(listik)

Analit = {}

for j in listik:
        Analit[j]=[]

for i in MY_list:
    print(i)
    for j in listik:
        Analit[j].append(i[1][j])

for i in Analit:
    Analit[i] = list(set(Analit[i]))
    print(i, Analit[i])