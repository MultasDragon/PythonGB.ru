# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 21:42:42 2022

@author: asarlybayev
"""
#тут была неудачная попытка установить сторонний модуль на нашу волшебную корпоративную компутирняку, она провалилась
#from translate import Translator
#translator= Translator(from_lang="german",to_lang="spanish")
#translation = translator.translate("Guten Morgen")
#print(translation)

Translatore = {
            'One': 'Раз',
            'Two': 'Два',
            'Three': 'Три',
            'Four': 'Четыре',
            'Five': 'Пять',
            'Six': 'Шесть',
            'Seven': 'Семь',
            'Eight': 'Восемь',
            'Nine': 'Девять',
            'Ten': 'Десять'
            }
trans = list(Translatore)

#print(Translatore)
#print(trans)
with open('HoakinPhoenix.txt', 'r', encoding='utf-8') as re:
    with open('HoakinPhoenix_translation.txt', 'w', encoding='utf-8') as wr:
        for i in re.readlines():
            for j in i.split(" "):
                if j in Translatore:
                    i = i.replace(j, Translatore[j])
            print(i.replace("\n",""), file = wr)
        print('\nВышел зайчик погулять\nСмотрит раз, смотрит два,\nПроморгал лису - Звизда!', file = wr)