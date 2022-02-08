# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:16:06 2022

@author: asarlybayev
"""

Sez = ["Зима", "Весна", "Лето", "Осень"]

Austr_Sez_dict = {7: "Зима", 8: "Зима", 9: "Весна", 10: "Весна", 11: "Весна", 12: "Лето", 1: "Лето", 2: "Лето", 3: "Осень", 4: "Осень", 5: "Осень", 6: "Зима"}

Temp = ["холодно", "уже теплеет", "тепло", "уже холодает"]
#0 1 2 3
#2 3 0 1

Okonec = ["';..;'", "ый", "ой", "ий", "ый", "ый", "ой", "ой", "ой", "ый", "ый", "ый", "ый"]

Mesyaz = input("Введите, пожалуйста, номер месяца в виде целого числа без лишних знаков: ")
J = ""
for I in Mesyaz:
    if I in '0123456789':
        J = J + I
if int(J) % 12 == 0:
    Mesyaz = 12
else:
    Mesyaz = int(J) % 12

I = Mesyaz // 3 % 4
J = (I + 2) % 4

print(f"{Mesyaz}{Okonec[Mesyaz]} месяц относится к сезону {Sez[I]}, у нас уже {Temp[I]}, а в Австралии в это время - {Austr_Sez_dict[Mesyaz]}, у них {Temp[J]}")