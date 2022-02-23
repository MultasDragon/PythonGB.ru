# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 17:28:28 2022

@author: asarlybayev
"""

from random import randint
from json import dump
list_firms = ["Рога_и_Копыта",
               "Копытные",
               "Рогатые",
               "Итые",
               "Итые_Рогатые",
               "Итые_Копытные",
               "Рогатые_но_не_Копытные",
               "Копытные_но_не_Рогатые"]
list_proprietations = ["ООО", "ЗАО", "ТОО", "ОАО", "ЯНАО", "НПГФ", "ТОО_СП", "ИП", "АО"]
#js=[]
#for i in list_firms:
#    j1 = randint(0, len(list_proprietations)-1)
#    js.append([i, list_proprietations[j1], randint(1000, 10000), randint(1000, 10000)])
js = [[i, list_proprietations[randint(0, len(list_proprietations)-1)], randint(1000, 10000), randint(1000, 10000)] for i in list_firms]
with open("HoakinPhoenix_7.txt", "w", encoding="utf-8") as wr:
    for i in js:
        print(*i, file=wr)

ap={}
with open("HoakinPhoenix_7.txt", "r", encoding="utf-8") as re:
    ap = 0.0
    cou = 0
    list_firms = {i.split(" ")[0]: float(i.split(" ")[2]) - float(i.split(" ")[3]) for i in re.readlines()}
    for i in list_firms.values():
        ap += i if i > 0 else 0
        cou += 1 if i > 0 else 0
    list_firms = [list_firms, {"average_profit": ap/cou}]
    dump(list_firms, open("HoakinPhoenix_7.json", "w", encoding="utf-8"), ensure_ascii = False, indent = 2)