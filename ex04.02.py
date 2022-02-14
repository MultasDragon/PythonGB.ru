# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 18:39:55 2022

@author: asarlybayev

2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


from itertools import islice
asd = [300, 2, 4, 15, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
asd_new = (i for i in asd)
asd_form =[]
#j = asd_new
#print(*islice(j, 100))
i = next(asd_new)
while True:
    try:
        i1 = next(asd_new)
        if i < i1:
            asd_form.append(i1)
        i = i1        
    except:
        break
print(asd_form)
#print(*islice(j, 100))