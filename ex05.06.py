# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:24:18 2022

@author: asarlybayev
"""

from random import randint
list_topics = ["Физика",
               "Информатика",
               "Проприетатор",
               "Физкультура",
               "Основа теории Слова",
               "Физика ядрённых частиц и их применение",
               "Концепция Слова Божьего против Неосознанных Флуктуаций Эфира"]
list_lessons = [["(л)", "(пр)", "(лаб)"],
                ["(л)", "-", "(пр)"],
                ["(пр)", "(лаб)", "-"],
                ["(л)", "-", "(лаб)"]]
"""js = {i: [str(randint(10, 50)) + list_lessons[j1][j2] if list_lessons[j1][j2] != "-" else "-" for j2 in range(3)] for zip(i, j1) in list_topics, randint(0,3)}
подскажете потом как компрехеншенс тут скоррекитровать, чтобы получился код внизу"""
js={}
for i in list_topics:
    j1 = randint(0,3)
    k = []
    for j2 in range(3):
        trick = str(randint(10, 50)) + list_lessons[j1][j2] if list_lessons[j1][j2] != "-" else list_lessons[j1][j2]
        k.append(trick)
    js[i] = k
with open("HoakinPhoenix_6.txt", "w", encoding="utf-8") as wr:
    for i in js:
        print(f'{i}:', *js[i], file=wr)

sumo = {}
with open("HoakinPhoenix_6.txt", "r", encoding="utf-8") as re:
#    print(re.read())
#    re.seek(0)
    for i in re.readlines():
        iLiter = i.find(":")
        grep = i[:iLiter]
        sumo[grep] = 0
        j = ""
        while iLiter < len(i):
            if i[iLiter].isnumeric():
                j = j + i[iLiter]
#                print('j = ', j)
            elif len(j) > 0:
                sumo[grep] += int(j)
                j = ""
#                print('j = ', j)
#                print('sumo = ', sumo)
            iLiter += 1

print('Коллекция: ', sumo)