print("Digite o número a ser convertido para base 10:")
valor = int(input())

print("Digite a base:")
baseN = int(input())

continuar = True
aux = valor
while continuar:
    quociente = int(aux / baseN)
    resto = int(aux % baseN)
    print(str(resto),end="")
    aux = quociente
    if quociente < baseN:
        continuar = False
        print(str(quociente),end="")

