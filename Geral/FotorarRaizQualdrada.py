def raizQuadradaPerfeita(numero):
    for i in range(2 , int(float(numero)/2 + 1) ):
        if i**2 == int(numero):
            return i
    return 0

def fatorarNumero(num):
    print(str(num)+" = ",end = "")
    k = 2
    while k < num:
        raizNumero = raizQuadradaPerfeita(k)
        if(raizNumero > 0 and num % k == 0):
            print(str(raizNumero)+".",end = "")
            num = num / k
            k = 1
        else:
            k = k + 1
    print("sqrt("+str(int(num))+")")

def interagirUsuario():
    continuar = True
    while continuar:
        print("Digite o número inteiro maior que 0 para fatorar:(0 ou negativo para encenrrar)")
        valor = int(input())
        if valor > 0:
            fatorarNumero(valor)
        else:
            print("Programa encerrado!")
            continuar = False

interagirUsuario()