import math



a = [1,434,5,55,55,23,23,23,34,23,123,123,555]
print(a)

a.append(34)
print(a)

a.remove(434)
print(a)

a.insert(1,325435)
print(a)

a.insert(400,55)
print(a)

print("Comprimento da lista: "+ str(len(a)))
print(len(a))

print(a.count(23))

print(a.index(23))

if a.count(555) > 0:
    print("----", end="\n")
    print(a.index(555))

def procurarComWhile(lista, numero):
    i = 0
    continuar = True
    while continuar:
        if(lista[i] == numero):
            return i
            continuar = False
        i = i + 1
    return -1

def procurarComFor(lista, numero):
    for i in range (len(lista)):
        if(lista[i] == numero):
            return i
    return -1

def procurarAlternativo(lista, valor):
    for(i, v) in enumerate(lista):
        if(v == valor):
            return i
    return -1

def search(list, number):
    if(list.count(number) > 0):
        return list.index(number)
    else:
        return -1

print("-----")

print(search(a,555))
print(procurarComWhile(a,555))
print(procurarComFor(a,555))
print(procurarAlternativo(a,555))

print("-----")

def contar(lista, valor):
    total = 0
    for v in lista:
        if v == valor:
            total += 1
    return total

print(contar(a,55))

a = [1,2,3,4,7,9,23,24,35,37,122,125,555]
i = 556
while i < 1601:
    a.append(i)
    i += 1

b = [1]

print("---!!0--")

def pesquisaDicotomica(list, num):
    min = 0
    max = len(list) - 1
    mid = 0
    count = 0
    while True:
        if num == list[mid]:
            print(count)
            return mid
        elif max - min < 2:
            print(count)
            return -1
        else:
            mid = (max + min) // 2
            count += 1
            if num > list[mid]:
                min = mid
            else:
                max = mid
    print(count)
    return -1

print(pesquisaDicotomica(a, 1002))