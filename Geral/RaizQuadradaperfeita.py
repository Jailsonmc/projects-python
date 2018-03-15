
print("Digite um número para obter uma raiz perfeita:")
num = int(input())
print("Digite o índice da raiz:")
n = int(input())
temRaizPerfeita = False
indice = 0

for i in range(2 , int(float(num)/2 + 1) ):
    if i**n == num:
        temRaizPerfeita = True
        indice = i

if temRaizPerfeita:
    print("A raiz {}º perfeita de {} é {}".format(str(n),str(num),str(indice)))
    print("A raiz "+str(n)+"º perfeita de "+str(num)+" é " +str(indice))
else:
    print(str(num)+" não tem raiz "+str(n)+"º perfeita. ")