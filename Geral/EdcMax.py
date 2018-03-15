
##Exemplo 1

c = [3,2,14,16,1]
print(c)
max = c[0]
for i in range (1, len(c)):
    if max < c[i]:
        max = c[i]
print(max, "É o máximo da sequência dada")

import random
f = 0
while f < 100000:
    c = random.sample(range(2),1)
    f += 1
b = False
for i in range(0, len(c)):
    if c[i] == 2:
        b = True
if b == True:
    print("Achei")
else:
    pass
print("Não Achei")

max = c[0]
for i in range(1, len(c)):
    if max < c [i]:
        max = c[i]
print(max, "É o máximo da sequência dada")

##Exemplo 2

x = 3
a = [4,2,3,7,1]
i = 0
while i <= len(a) and x != a[i]:
    i = i + 1
if i < len(a):
    location = i + 1
else:
    location = 0
print(location)

##Exemplo 3

#sort = random.sample(range(1000,200))

##Exemplo 4

def potencia(a,n):
    """Calcula a**n recursivamente"""
    if n == 0:
        return 1
    else:
        return a * potencia( a, n -1 )

print(potencia(10,3))

def potencia2(a,n):
    """Cal"""
    pot = 1
    for i in range(n):
        pot = a * pot
    return pot

print(potencia2(5,2))

##Exemplo 5

def fibonacciRecursivo(n):
    """Calu"""
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacciRecursivo(n-1) + fibonacciRecursivo(n-2)

print(fibonacciRecursivo(10))

def fibonacci(n):
    a , b = 0 , 1
    for i in range (n-1):
        a , b = b , a + b
    return b
print(fibonacci(10))

c = null
print(c)