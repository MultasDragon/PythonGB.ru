# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:19:57 2022

@author: asarlybayev
"""
moi_liste = input('Введите элементы списка через пробел: ').split()
print("Первый список: ", moi_liste)


for i in range(0, len(moi_liste)-1, 2):
    moi_liste[i], moi_liste[i + 1] = moi_liste[i + 1], moi_liste[i]
print("Первый список переставлен: ", moi_liste)

moi_listd = []
elem = input("Введите первый элемент следующего списка: ")
while len(elem) > 0:
    moi_listd.append(elem)
    elem = input('Введите следуюший элемент списка, если же закончено, просто нажмите энтер: ')
print("Второй список: ", moi_listd)


elem = moi_listd[::2]
elem1 = moi_listd[1::2]

Shyutka = "["
for i in range(len(moi_listd) // 2):
    Shyutka = Shyutka + "'" + elem1[i] + "', '" + elem[i] + "', "
if len(moi_listd) % 2 == 0:
    Shyutka = Shyutka[:-2] + "]"
else:
    Shyutka = Shyutka + "'" + elem[-1] + "']"

moi_listd = Shyutka[2:-2].split("', '")

print("Второй список переставлен: ", moi_listd)
print(Shyutka)
print(elem)
print(elem1)
