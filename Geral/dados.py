



pasta ="/Users/jailsoncavalcanti/Doc/Projects/Python/dados/"

ficheiro = open(pasta + "dados01.txt","w+")

soma = 0
for i in range(10):
    soma = soma + 1
    ficheiro.write(str(i)+" "+str(soma) + "\n")
ficheiro.close()

ficheiro = open(pasta+"dados01.txt", "a+")
#ficheiro.write(" -    ------   -- ")
ficheiro.close()


soma = 0
ficheiro = open(pasta+"dados01.txt", "r+")
for linha in ficheiro.readlines():
    if linha[0] != "-":
        col1 = int(linha.split(" ")[0])
        soma += col1
ficheiro.close()
print("A soma é :",soma)

soma1 = 0
soma2 = 0
ficheiro = open(pasta+"dados01.txt", "r+")
for linha in ficheiro.readlines():
    if linha[0] != "-":
        col1 = int(linha.split(" ")[0])
        soma1 += col1
        col2 = int(linha.split(" ")[1])
        soma2 += col2
ficheiro.close()
print("A soma é :",soma1," sss ", soma2)




x = "10a20a30a40"
lista = x.split("a")
print(lista)



