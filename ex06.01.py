# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:43:40 2022

@author: asarlybayev
"""
import time

class TrafficLight:
    __going_cycle = (("green", "yellow", "red", "yellow"), (7, 2, 7, 2))
    def __init__(self):
        self.__state = 1
        self.__color = TrafficLight.__going_cycle[0][self.__state]
    def running(self, order = 0, leng = 20):
        beg = time.time()
        while time.time() - leng < beg:
            order %= 4
            self.__color = TrafficLight.__going_cycle[0][order]
            print(*time.localtime()[3:6], self.__color, sep= ":")
            time.sleep(TrafficLight.__going_cycle[1][order])
            order += 1
#    def status(self):
        

TL1 = TrafficLight()
TL1.running()