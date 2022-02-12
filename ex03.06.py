# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 23:08:18 2022

@author: asarlybayev
#6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой. 
Например, print(int_func(‘text’)) -> Text.
7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. Каждое слово состоит из латинских 
букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте написанную 
ранее функцию int_func().
"""
#def int_func(*args):
#    krya = list(args)
#    for i in range(len(krya)):
#        krya[i] = krya[i].title()
#    return krya
def int_func(iStroka):
    iList2 = []
    while "  " in iStroka:
        iStroka = iStroka.replace("  "," ")    
    iList = iStroka.split(" ")
    for iWord in iList:
        iASCII = list(map(ord, list(iWord)))
        if ord("a") <= min(iASCII) and ord("z") >= max(iASCII):
            iList2.append(iWord.title())
    return iList2


print(' '.join(map(str, int_func(input('Введите букафки на нерусском: ')))))
