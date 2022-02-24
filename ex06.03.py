# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:14:23 2022

@author: asarlybayev
"""

class Worker:
    def __init__(self, n, sn, pos, wage, bonus):
        self.name = n
        self.surname = sn
        self.position = pos
        self.__income = {"wage": float(wage), "bonus": float(bonus)}
        self._income = {"wage": float(wage), "bonus": float(bonus)}
    def get_incomes(self):
        return self.__income

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname
    def get_total_income(self):
        return self._Worker__income["wage"] + self._income["bonus"]
    def get_total_income1(self):
        k=0
        for i in self.get_incomes().values():
            k += i
        return k

Leader = Position('Леонид', 'Леонтьев', 'Инженер инфраструктуры', '15000', '200000')
print(Leader.name)
print(Leader.get_full_name())
print(Leader.get_total_income())
print(Leader.get_total_income1())