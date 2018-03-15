import math

#soma = 5

#for i in range(10):
#  soma = soma + 1
#print(soma)


#print("Escreva a base:")
#base = int(input())
#print("Escreva a altura:")
#altura = int(input())

#h = math.sqrt(base**2 + altura**2)
#print("O valor da hipotenusa é: " + str(h))


def isPrime(num):
    for i in range(2, int(math.sqrt(num)) +1 ):
        if (num % i == 0):
            return False
    return True

def primes(number):
    for i in range( 2 , number + 1):
        if isPrime(i):
            print(str(i) +" É primo")

#print("Escreva um número:")
#num = int(input())

#primes(num)

sair = False
media = 0
soma = 0
while sair != True:
    print("Digite um valor:(Digite c para encerrar e calcular a média)")
    num = input()
    if(num == "c"):
        print(str(media))
        print(str(soma))
        sair = True
    else:
        media = (media + float(num)) / 2
        soma = soma + float(num)

#pedra,papel , tesoura  / raiz quadrada / 12 = sqrt(12) = 2.sqrt(3)




