# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 23:38:07 2022

@author: asarlybayev
"""

class Stationery:
    def __init__(self, n):
        self.title = n
    def draw(self):
        print(f'{self.title} начал отрисовку')

class Pen(Stationery):
    def draw(self):
        print(f'Ручка {self.title} начал отрисовку')

class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш {self.title} начал отрисовку')

class Handle(Stationery):
    def draw(self):
        print(f'Ручкамалярка {self.title} начал отрисовку')

Peredmety = [Stationery("Хрякалка"), Pen("Ручкалка"), Pencil("Карандашилка"), Handle("Малярунок")]
for i in Peredmety:
    i.draw()