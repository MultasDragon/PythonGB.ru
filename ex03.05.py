# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 21:45:32 2022

@author: asarlybayev
5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться 
к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён после нескольких 
чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def poiskator(YA_STROKA, YA_SUMMATOR = 0):    
    YA_STROKA = YA_STROKA.replace(",",".")
    while not(YA_STROKA.upper().replace("N","").replace(" ","").replace(".","").replace("-","").replace("+","").isdigit()):
        if YA_STROKA.upper() == "N":
            print(f'В итоге сумма {YA_SUMMATOR:.3f}')
            return
        YA_STROKA = input('Ну позязя!!! ').replace(",",".")
    while "  " in YA_STROKA:
        YA_STROKA = YA_STROKA.replace("  "," ")
    while YA_STROKA.upper() != "N":        
        YA_list = YA_STROKA.split(" ")
        for i in YA_list:            
            if i.replace(".","").replace("-","").replace("+","").isdigit():
                YA_SUMMATOR += float(i)
            else:
                YA_STROKA = "N"
                if i.upper() == "N":
                    print(f'В итоге сумма {YA_SUMMATOR:.3f}')
                    return
                j = 0
                while j < len(i):
                    if i[j].upper() != "N":
                        j += 1
                    else:
                        break                
                YA_SUMMATOR += float(i[:j])
                print(f'В итоге сумма {YA_SUMMATOR:.3f}')
                return
        return poiskator(input(f'Текущая сумма {YA_SUMMATOR:.3f}, продолжим ввод (N - прекращаем)? '), YA_SUMMATOR)
    

poiskator(input('Введите числа, разделенные пробелом, при вводе буквы "N", алгоритм прекратит алгоритмить: '))
