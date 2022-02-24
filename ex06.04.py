# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 21:44:43 2022

@author: asarlybayev
"""

class Car:
    def __init__(self, n):
        self.name = n
    def go(self):
        print(f'Машина {self.name} поехала, честно')
    def stop(self):
        print(f'Машина {self.name} токтановилась, вроде бы...')
    def turn(self, direction):
        print(f'Машина {self.name} павернулася, я видел, туда - {direction}')
    def show_speed(self, speed):
        print(f'Скорость машины {self.name} - {speed}, я сам лично мерил!')

class TownCar(Car):
    def show_speed(self, speed):
        if speed > 60:
            print(f'Леди и джентльмены, а также не определившиеся до конца, по городу не двигаются выше 60')
        else:
            print(f'Скорость машины {self.name} - {speed}, я сам лично мерил!')
    
class WorkCar(Car):
    def show_speed(self, speed):
        if speed > 40:
            print(f'Господа Рабочие, на рабочем транспорте не двигаются выше 40')
        else:
            print(f'Скорость машины {self.name} - {speed}, я сам лично мерил!')

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

fignyacary = [TownCar("Фигня Таун Кар"), SportCar("Фигня Спорт Кар"), WorkCar("Фигня Рабоче Кар"), PoliceCar("Фигня МентоКар")]
for i in fignyacary:
    i.go()
    i.show_speed(30)
    i.turn("Влево")
    i.show_speed(50)
    i.turn("Вправо")
    i.show_speed(70)
    i.stop()