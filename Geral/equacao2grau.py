import math

print("Digite o índice 2:")
indice2 = int(input())

print("Digite o índice 1:")
indice1 = int(input())

print("Digite a constante:")
constante = int(input())

delta = (indice1*indice1 - 4*indice2*constante)
raiz1 = ( - indice1 - math.sqrt(delta) ) / (2 * indice2)
raiz2 = ( - indice1 + math.sqrt(delta) ) / (2 * indice2)

print(raiz1)
print(raiz2)