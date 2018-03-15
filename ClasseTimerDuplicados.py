# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 01:12:13 2018

@author: Paulo Enes Silveira
"""

import time
import random
import gc
 
class MeasureDuration:
    def __init__(self):
        self.start = None
        self.end = None
 
    def __enter__(self):
        self.start = time.time()
        return self
 
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print ('Total time taken: {}'.format (self.duration()))
 
    def duration(self):
        return str((self.end - self.start) * 1000) + ' milliseconds'
    
    

def gera_lista(tamanho, inf, sup):
    return [random.randint(inf,sup) for i in range(tamanho)]

def duplicados_1(lista):
    tamanho=len(lista)
    for i in range(tamanho-1):
        for j in  range(i+1,tamanho):
            if lista[i] == lista[j]:
                print (True)
                return True
    print (False)
    return False

def duplicados_2(lista):
    tamanho=len(lista)
    aux=[0]*tamanho
    for i  in range (tamanho):
        if aux[lista[i]] != 0:
            print (True)
            return True
        else:
            aux[lista[i]]=1
    print (False)
    return False

if __name__=='__main__':
    gc.disable()
    
    lista_1=gera_lista(10000000,1,7500000)
#    print (lista_1,'\n\n')

    with MeasureDuration() as m:
        duplicados_1(lista_1)

    with MeasureDuration() as m:
        duplicados_2(lista_1)
        
#  gc.disable()
    
    with MeasureDuration() as m:
        duplicados_1(lista_1)

    with MeasureDuration() as m:
        duplicados_2(lista_1)
        