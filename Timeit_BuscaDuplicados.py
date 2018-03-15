# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:00:44 2018

@author: Paulo Enes Silveira/from:

"""

# importing the required modules
import timeit
 
# Busca duplicados 1 - na mesma lista
def duplicados_1(lista):
    tamanho=len(lista)
    for i in range(tamanho-1):
        for j in  range(i+1,tamanho):
            if lista[i] == lista[j]:
                return True
    return False
 
 
# Busca duplicados 2 - na mesma lista com auxilio lista auxiliar
def duplicados_2(lista):
    tamanho=len(lista)
    aux=[0]*tamanho
    for i  in range (tamanho):
        if aux[lista[i]] != 0:
            return True
        else:
            aux[lista[i]]=1
    return False
 
 
# Calcula tempo da Busca duplicados 1
def tempo_busca_dupli_1():
    SETUP_CODE = '''
from __main__ import duplicados_1
from random import randint'''
 
    TEST_CODE = '''
lista = [randint(1,1500) for i in range(2000)]
duplicados_1(lista)'''
     
    # timeit.repeat statement
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 2000)
 
    # priniting minimum exec. time
    print(times)
    print('Tempo duplicados_1: {}'.format(min(times)))        
 
 
# Calcula tempo da Busca duplicados 2
def tempo_busca_dupli_2():
    SETUP_CODE = '''
from __main__ import duplicados_2
from random import randint'''
     
    TEST_CODE = '''
lista = [randint(1,1500) for i in range(2000)]
duplicados_2(lista)
    '''
    # timeit.repeat statement
    times = timeit.repeat(setup = SETUP_CODE,
                          stmt = TEST_CODE,
                          repeat = 3,
                          number = 2000)
 
    # priniting minimum exec. time
    print (times)
    print('Tempo duplicados_2: {}'.format(min(times)))  
 
if __name__ == "__main__":
    tempo_busca_dupli_1()
    tempo_busca_dupli_2()
    