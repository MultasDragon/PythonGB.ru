# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:03:01 2022

@author: asarlybayev
"""

class Road:
    _length = 100.0
    _width = 3.0
    def __init__(self, l, w, h):
        self._length = l
        self._width = w
        self._height= h
        self.name = id(self)
        print(f'Асфальт {self.name} с параметрами {l}, {w}, {h} потребует {l*h*w*25/1000} т асфальта')


Trassa = Road(100, 3, 2)