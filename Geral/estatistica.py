
#ab = [1,434,5,55,55,23,23,23,34,23,123,123,555]
a = [3,6,2,1,4]

sum = 0
for i in range(len(a)):
    sum += a[i]
media = sum/len(a)
print(media)

sumDes = 0
for i in range(len(a)):
    if a[i] >= media:
        sumDes += (a[i] - media)*(a[i] - media)
    else:
        sumDes += (media - a[i])*(media - a[i])
desviopadrao = sumDes / len(a)
print(desviopadrao)
####################

def media(V):
    soma = 0
    for x in V:
        soma += x
    return soma / len(V)

def difQuadradas(V,m):
    diferencas = []
    for x in V:
        diferencas.append((x-m)**2)
    return diferencas
def variancia(V):
    return media(difQuadradas(V, media(V)))

A = [3,6,2,1,4]
print(media(A))
print(variancia(A))

######
def primeirasLetras(v):
    letras = []
    for a in v:
        letras.append(a[0])
    return letras
b = ["gol","sexta","colarinho","Texto","PAlavra2"]
print(primeirasLetras(b))

##Exercícios
##1.Fazer um método que recebe duas listas de strings e calcula o número de elementos comuns entre elas
##2.Fazer um método que recebe duas listas de strings e devolve uma outra lista com as palavras que não pertencem a ambas as listas
##3.Fazer um método que recebe uma listas de strings e conta as letras presentes em todas as strings
##4.Fazer um método que recebe uma lista de strings e devolve uma outra lista de strings formada pelas mesmas palavras sem os sinais de pontuação(!"#$%&/()=*?)