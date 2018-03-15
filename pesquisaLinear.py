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

def binary_search(mylist, find):
    #count = 0
    #result = [ 0, False]
    while len(mylist) > 0:
        mid = (len(mylist))//2
        #print("mid=",mid)
        #count = count + 1
        if mylist[mid] == find:
            #result[0] = count
            #result[1] = True
            return True
            #return result
        elif find < mylist[mid]:
            mylist = mylist[:mid]
        else:
            mylist = mylist[mid + 1:]
    #result[0] = count
    #result[1] = False
    #return result
    return False

def linear_search(mylist, find):
    #count = 0
    #result = [ 0, False, 0]
    for x in mylist:
        #print(x, " - " ,count)
        if x == find:
            #result[0] = count
            #result[1] = True
            #return result
            return True
        #count = count + 1
    #result[0] = count
    #result[1] = False
    #return result
    return False

print("Arranque!")
list = []

listPequena = [ 2, 3123, 4, 34, 554, 234, 234 ]

tamanho = 1000001
lista = [x for x in range(tamanho)]

listPequena.sort()

#tamanho = 1000000
#for i in range(tamanho):
#    list.append(random.randint(0, 1000000))
#print("Gerado Lista de:",tamanho ," posições.")
#list.sort()




#print(binary_search(list, 100))

#print(linear_search(list, 100))




def foo():
    time.sleep(1)

if __name__=='__main__':
    gc.disable()

    lista_1=gera_lista(10000000,1,7500000)
    #    print (lista_1,'\n\n')

    with MeasureDuration() as m:
        binary_search(lista, 2)

    with MeasureDuration() as m:
        linear_search(lista, 2)

    with MeasureDuration() as m:
        binary_search(lista, len(lista)-1)

    with MeasureDuration() as m:
        linear_search(lista, len(lista)-1)

    with MeasureDuration() as m:
        binary_search(lista, len(lista)//2)

    with MeasureDuration() as m:
        linear_search(lista, len(lista)//2)

    #with MeasureDuration() as m:
    #    duplicados_1(lista_1)

    #with MeasureDuration() as m:
    #    duplicados_2(lista_1)

    #  gc.disable()

    #with MeasureDuration() as m:
    #    duplicados_1(lista_1)

    #with MeasureDuration() as m:
    #    duplicados_2(lista_1)